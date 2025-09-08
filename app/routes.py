# app/routes.py
from flask import render_template, request, redirect, url_for
from app import app
from app.models import todos

VALID_STATUSES = ["Started", "Pending", "Completed"]

@app.route("/")
def index():
    # render list (todos) into index.html
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task", "").strip()
    if task:
        todos.append({"task": task, "status": "Pending"})
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
    return redirect(url_for("index"))

@app.route("/status/<int:task_id>", methods=["POST"])
def update_status(task_id):
    if 0 <= task_id < len(todos):
        status = request.form.get("status")
        if status in VALID_STATUSES:
            todos[task_id]["status"] = status
    return redirect(url_for("index"))
