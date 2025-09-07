# app/routes.py
from flask import Flask, render_template, request, redirect, url_for
from app.models import todos

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        # Each task is now a dict with 'task' and 'completed' status
        todos.append({"task": task, "completed": False})
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
    return redirect(url_for("index"))

@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    if 0 <= task_id < len(todos):
        todos[task_id]["completed"] = not todos[task_id]["completed"]
    return redirect(url_for("index"))
