# test/test_app.py
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_add_and_toggle(client):
    # Add a task
    client.post("/add", data={"task": "Test Task"})
    response = client.get("/")
    assert b"Test Task" in response.data

    # Toggle the task
    client.get("/toggle/0")
    response = client.get("/")
    assert b"line-through" in response.data  # Completed task should be styled

def test_delete_task(client):
    # Add a task
    client.post("/add", data={"task": "Delete Me"})
    response = client.get("/")
    assert b"Delete Me" in response.data

    # Delete it
    client.get("/delete/0")
    response = client.get("/")
    assert b"Delete Me" not in response.data
