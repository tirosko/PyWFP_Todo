from datetime import datetime
import json
import os
from urllib.parse import urlsplit
import webbrowser
from threading import Timer

from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["TODO_FILE"] = os.path.join(app.root_path, "tasks.txt")


def load_todos():
    todos = []
    filename = app.config["TODO_FILE"]
    if not os.path.exists(filename):
        return todos

    with open(filename, "r", encoding="utf-8") as tasks_file:
        for line_number, line in enumerate(tasks_file, start=1):
            line = line.rstrip("\r\n")
            if not line:
                continue
            if line.startswith("{"):
                todo = json.loads(line)
                if not isinstance(todo, dict) or not isinstance(todo.get("done"), bool):
                    raise ValueError(f"Neplatná úloha v súbore {filename} na riadku {line_number}")
                todo.setdefault("text", "")
                todo.setdefault("due_at", "")
                todo.setdefault("description", "")
                todo.setdefault("location", "")
                todo.setdefault("url", "")
                todos.append(todo)
                continue
            done_value, remainder = line.split(";", 1)
            if done_value not in {"0", "1"}:
                raise ValueError(f"Neplatný stav úlohy v súbore {filename}")
            due_at = ""
            text = remainder
            if ";" in remainder:
                possible_due_at, possible_text = remainder.split(";", 1)
                try:
                    datetime.strptime(possible_due_at, "%Y-%m-%dT%H:%M")
                except ValueError:
                    pass
                else:
                    due_at = possible_due_at
                    text = possible_text
            todos.append({
                "text": text,
                "done": done_value == "1",
                "due_at": due_at,
                "description": "",
                "location": "",
                "url": "",
            })
    return todos


@app.template_filter("format_due_at")
def format_due_at(value):
    if not value:
        return ""
    return datetime.strptime(value, "%Y-%m-%dT%H:%M").strftime("%d.%m.%Y %H:%M")


def save_todos(todos):
    with open(app.config["TODO_FILE"], "w", encoding="utf-8") as tasks_file:
        for todo in todos:
            tasks_file.write(f"{json.dumps(todo, ensure_ascii=False)}\n")


def parse_due_at(due_at):
    if not due_at:
        return ""
    try:
        parsed_due_at = datetime.strptime(due_at, "%Y-%m-%dT%H:%M")
    except ValueError:
        abort(400, description="Zadaný termín nie je platný.")
    if parsed_due_at.minute % 5:
        abort(400, description="Minúty musia byť v 5-minútových intervaloch.")
    return parsed_due_at.strftime("%Y-%m-%dT%H:%M")


def parse_task_url(value):
    value = value.strip()
    if not value:
        return ""
    parsed_url = urlsplit(value)
    if parsed_url.scheme not in {"http", "https"} or not parsed_url.hostname:
        abort(400, description="URL musí začínať na http:// alebo https://.")
    return value


@app.route("/")
def index():
    todos = load_todos()
    now = datetime.now()
    today_key = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%Y-%m-%dT%H:%M")
    active_todos = [todo for todo in todos if not todo["done"]]
    scheduled_todos = [todo for todo in active_todos if todo["due_at"]]
    overdue_count = sum(todo["due_at"] < current_time for todo in scheduled_todos)
    upcoming_tasks = sorted(
        (todo for todo in scheduled_todos if todo["due_at"] >= current_time),
        key=lambda todo: todo["due_at"],
    )
    weekday_names = (
        "pondelok", "utorok", "streda", "štvrtok", "piatok", "sobota", "nedeľa",
    )
    month_names = (
        "január", "február", "marec", "apríl", "máj", "jún",
        "júl", "august", "september", "október", "november", "december",
    )
    today_label = (
        f"{weekday_names[now.weekday()]}, {now.day}. "
        f"{month_names[now.month - 1]} {now.year}"
    )
    return render_template(
        "dashboard.html",
        today_label=today_label,
        today_count=sum(
            todo["due_at"].startswith(today_key)
            for todo in active_todos
            if todo["due_at"]
        ),
        scheduled_count=len(scheduled_todos),
        overdue_count=overdue_count,
        total_count=len(todos),
        active_count=len(active_todos),
        completed_count=len(todos) - len(active_todos),
        completion_percent=round((len(todos) - len(active_todos)) / len(todos) * 100)
        if todos else 0,
        upcoming_tasks=upcoming_tasks[:5],
        open_add_dialog=request.args.get("open_add") == "1",
    )


@app.route("/tasks")
def tasks():
    todos = load_todos()
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%dT%H:%M")
    today_key = now.strftime("%Y-%m-%d")
    view = request.args.get("view", "all")
    task_titles = {
        "all": "Moje úlohy",
        "today": "Dnes",
        "scheduled": "Naplánované úlohy",
        "completed": "Dokončené úlohy",
        "overdue": "Úlohy po termíne",
    }
    if view not in task_titles:
        abort(404, description="Požadovaný zoznam úloh neexistuje.")

    def is_visible(todo):
        if view == "today":
            return not todo["done"] and todo["due_at"].startswith(today_key)
        if view == "scheduled":
            return not todo["done"] and bool(todo["due_at"])
        if view == "completed":
            return todo["done"]
        if view == "overdue":
            return not todo["done"] and bool(todo["due_at"]) and todo["due_at"] < current_time
        return True

    display_todos = [
        {**todo, "task_idx": idx}
        for idx, todo in enumerate(todos)
        if is_visible(todo)
    ]
    display_todos.sort(key=lambda todo: (not todo["due_at"], todo["due_at"]))
    schedule_tasks = [
        {
            **todo,
            "edit_url": url_for("edit", idx=idx),
            "reschedule_url": url_for("reschedule", idx=idx),
        }
        for idx, todo in enumerate(todos)
    ]
    return render_template(
        "index.html",
        todos=display_todos,
        schedule_tasks=schedule_tasks,
        task_title=task_titles[view],
        view=view,
        open_add_dialog=request.args.get("open_add") == "1",
        today_count=sum(
            not todo["done"] and todo["due_at"].startswith(today_key)
            for todo in todos
            if todo["due_at"]
        ),
    )


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("todo", "").strip()
    due_at = request.form.get("due_at", "").strip()
    if text:
        due_at = parse_due_at(due_at)
        task_url = parse_task_url(request.form.get("url", ""))
        todos = load_todos()
        todos.append({
            "text": text,
            "done": False,
            "due_at": due_at,
            "description": request.form.get("description", "").strip(),
            "location": request.form.get("location", "").strip(),
            "url": task_url,
        })
        save_todos(todos)
    if request.form.get("return_to") == "dashboard":
        return redirect(url_for("index"))
    return redirect(url_for("tasks"))


@app.route("/edit/<int:idx>", methods=["POST"])
def edit(idx):
    todos = load_todos()
    if idx < 0 or idx >= len(todos):
        abort(404)
    text = request.form.get("todo", "").strip()
    if not text:
        abort(400, description="Názov úlohy nesmie byť prázdny.")
    due_at = parse_due_at(request.form.get("due_at", "").strip())
    task_url = parse_task_url(request.form.get("url", ""))
    todos[idx]["text"] = text
    todos[idx]["due_at"] = due_at
    todos[idx]["description"] = request.form.get("description", "").strip()
    todos[idx]["location"] = request.form.get("location", "").strip()
    todos[idx]["url"] = task_url
    save_todos(todos)
    return redirect(url_for("tasks"))


@app.route("/reschedule/<int:idx>", methods=["POST"])
def reschedule(idx):
    todos = load_todos()
    if idx < 0 or idx >= len(todos):
        abort(404)
    due_at = parse_due_at(request.form.get("due_at", "").strip())
    if not due_at:
        abort(400, description="Úloha musí mať zadaný termín.")
    todos[idx]["due_at"] = due_at
    save_todos(todos)
    return redirect(url_for("tasks"))


@app.route("/toggle/<int:idx>", methods=["POST"])
def toggle(idx):
    todos = load_todos()
    if idx < 0 or idx >= len(todos):
        abort(404)
    todos[idx]["done"] = not todos[idx]["done"]
    save_todos(todos)
    return redirect(url_for("tasks"))


@app.route("/delete/<int:idx>", methods=["POST"])
def delete(idx):
    todos = load_todos()
    if idx < 0 or idx >= len(todos):
        abort(404)
    todos.pop(idx)
    save_todos(todos)
    return redirect(url_for("tasks"))


if __name__ == "__main__":
    Timer(1, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(host="127.0.0.1", port=5000)
