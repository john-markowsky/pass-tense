from fastapi.testclient import TestClient
from app.api.users import router
from main import app


client = TestClient(router)

def test_post_register():
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "password": "123456",
        "user_type": "patient"
    }
    response = client.post("/register", json=data)
    assert response.status_code == 200

def test_get_register():
    with TestClient(app) as client:
        response = client.get("/register")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        assert "register" in response.text