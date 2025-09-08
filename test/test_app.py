import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "testkey"
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_add_and_toggle(client):
    # Add a task
    client.post("/add", data={"task": "Test Task"}, follow_redirects=True)
    response = client.get("/")
    assert b"Test Task" in response.data

    # Toggle the task
    client.get("/toggle/0", follow_redirects=True)
    response = client.get("/")
    assert b"line-through" in response.data  # task should appear completed

    # Check session directly
    with client.session_transaction() as sess:
        assert sess["todos"][0]["status"] == "completed"

def test_delete_task(client):
    # Add a task
    client.post("/add", data={"task": "Delete Me"}, follow_redirects=True)
    response = client.get("/")
    assert b"Delete Me" in response.data

    # Delete the task
    client.get("/delete/0", follow_redirects=True)
    response = client.get("/")
    assert b"Delete Me" not in response.data

    # Check session directly
    with client.session_transaction() as sess:
        assert sess["todos"] == []
