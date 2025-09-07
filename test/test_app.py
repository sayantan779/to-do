from app.routes import app

def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"My To-Do List" in response.data  # Changed from 'Hello'

def test_add_and_toggle():
    client = app.test_client()
    
    # Add a task
    client.post("/add", data={"task": "Test Task"})
    response = client.get("/")
    assert b"Test Task" in response.data
    
    # Toggle the task
    client.get("/toggle/0")
    response = client.get("/")
    assert b"line-through" in response.data  # The task should now be marked completed
