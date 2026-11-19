from datetime import datetime
import os

from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["TODO_FILE"] = os.path.join(app.root_path, "tasks.txt")


def load_todos():
    todos = []
    filename = app.config["TODO_FILE"]
    if not os.path.exists(filename):
        return todos

    with open(filename, "r", encoding="utf-8") as tasks_file:
        for line in tasks_file:
            line = line.rstrip("\r\n")
            if not line:
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
            todos.append({"text": text, "done": done_value == "1", "due_at": due_at})
    return todos


@app.template_filter("format_due_at")
def format_due_at(value):
    if not value:
        return ""
    return datetime.strptime(value, "%Y-%m-%dT%H:%M").strftime("%d.%m.%Y %H:%M")


def save_todos(todos):
    with open(app.config["TODO_FILE"], "w", encoding="utf-8") as tasks_file:
        for todo in todos:
            done_value = "1" if todo["done"] else "0"
            if todo["due_at"]:
                tasks_file.write(f"{done_value};{todo['due_at']};{todo['text']}\n")
            else:
                tasks_file.write(f"{done_value};{todo['text']}\n")


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


@app.route("/")
def index():
    todos = load_todos()
    schedule_tasks = [
        {
            **todo,
            "edit_url": url_for("edit", idx=idx),
            "reschedule_url": url_for("reschedule", idx=idx),
        }
        for idx, todo in enumerate(todos)
    ]
    return render_template("index.html", todos=todos, schedule_tasks=schedule_tasks)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("todo", "").strip()
    due_at = request.form.get("due_at", "").strip()
    if text:
        due_at = parse_due_at(due_at)
        todos = load_todos()
        todos.append({"text": text, "done": False, "due_at": due_at})
        save_todos(todos)
    return redirect(url_for("index"))


@app.route("/edit/<int:idx>", methods=["POST"])
def edit(idx):
    todos = load_todos()
    if idx < 0 or idx >= len(todos):
        abort(404)
    text = request.form.get("todo", "").strip()
    if not text:
        abort(400, description="Názov úlohy nesmie byť prázdny.")
    due_at = parse_due_at(request.form.get("due_at", "").strip())
    todos[idx]["text"] = text
    todos[idx]["due_at"] = due_at
    save_todos(todos)
    return redirect(url_for("index"))


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
    return redirect(url_for("index"))


@app.route("/toggle/<int:idx>", methods=["POST"])
def toggle(idx):
    todos = load_todos()
    if idx < 0 or idx >= len(todos):
        abort(404)
    todos[idx]["done"] = not todos[idx]["done"]
    save_todos(todos)
    return redirect(url_for("index"))


@app.route("/delete/<int:idx>", methods=["POST"])
def delete(idx):
    todos = load_todos()
    if idx < 0 or idx >= len(todos):
        abort(404)
    todos.pop(idx)
    save_todos(todos)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
