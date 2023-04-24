from fastapi.testclient import TestClient

from main import app


def test_index_endpoint():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        assert "Register" in response.text

def test_about_endpoint():
    with TestClient(app) as client:
        response = client.get("/about")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        assert "Register" in response.text

def test_dashboard_endpoint():
    with TestClient(app) as client:
        response = client.get("/dashboard")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        assert "Dashboard" in response.text
        assert "History" in response.text
        assert "Journal" in response.text
        assert "Doctor" in response.text

def test_login_endpoint():
    with TestClient(app) as client:
        response = client.get("/login")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        assert "register" in response.text