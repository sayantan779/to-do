from flask import Blueprint, render_template, request, redirect, url_for, session

main = Blueprint("main", __name__)

@main.before_app_request
def make_session_permanent():
    # Ensure todos exists in session
    if "todos" not in session:
        session["todos"] = []

@main.route("/")
def index():
    return render_template("index.html", todos=enumerate(session["todos"]))

@main.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        todos = session["todos"]
        todos.append({"task": task, "status": "pending"})
        session["todos"] = todos  # reassign to persist changes
    return redirect(url_for("main.index"))

@main.route("/toggle/<int:task_id>")
def toggle(task_id):
    todos = session["todos"]
    if 0 <= task_id < len(todos):
        if todos[task_id]["status"] == "completed":
            todos[task_id]["status"] = "pending"
        else:
            todos[task_id]["status"] = "completed"
        session["todos"] = todos
    return redirect(url_for("main.index"))

@main.route("/delete/<int:task_id>")
def delete(task_id):
    todos = session["todos"]
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
        session["todos"] = todos
    return redirect(url_for("main.index"))
