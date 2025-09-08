import pytest
from app import create_app
from app.models import todos

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"To-Do List" in response.data

def test_add_task(client):
    response = client.post("/add", data={"task": "Test Task"}, follow_redirects=True)
    assert response.status_code == 200
    assert any(todo["task"] == "Test Task" for todo in todos)

def test_update_task_status(client):
    # First add a task
    client.post("/add", data={"task": "Another Task"}, follow_redirects=True)
    task_id = len(todos) - 1

    # Now update status
    response = client.post(f"/update/{task_id}", data={"status": "completed"}, follow_redirects=True)
    assert response.status_code == 200
    assert todos[task_id]["status"] == "completed"

def test_delete_task(client):
    client.post("/add", data={"task": "Temp Task"}, follow_redirects=True)
    task_id = len(todos) - 1

    response = client.get(f"/delete/{task_id}", follow_redirects=True)
    assert response.status_code == 200
    assert all(todo["task"] != "Temp Task" for todo in todos)
