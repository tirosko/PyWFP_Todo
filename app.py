from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []  # jednoduchý zoznam úloh v pamäti

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("todo")
    if text:
        todos.append({"text": text, "done": False})
    return redirect(url_for("index"))

@app.route("/toggle/<int:idx>")
def toggle(idx):
    if 0 <= idx < len(todos):
        todos[idx]["done"] = not todos[idx]["done"]
    return redirect(url_for("index"))

@app.route("/delete/<int:idx>")
def delete(idx):
    if 0 <= idx < len(todos):
        todos.pop(idx)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
