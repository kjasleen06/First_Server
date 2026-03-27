from server_flask import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_json():
    client = app.test_client()
    response = client.get("/json")
    assert response.json["message"] == "Hello, JSON World!"