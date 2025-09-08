# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import todos

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html", todos=enumerate(todos))

@bp.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        todos.append({"task": task, "done": False})
    return redirect(url_for("main.index"))

@bp.route("/toggle/<int:task_id>")
def toggle(task_id):
    if 0 <= task_id < len(todos):
        todos[task_id]["done"] = not todos[task_id]["done"]
    return redirect(url_for("main.index"))

@bp.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
    return redirect(url_for("main.index"))
