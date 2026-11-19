from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_ticket():
    response = client.post(
        "/tickets",
        json={"title": "Login geht nicht", "description": "Seite lädt endlos"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Login geht nicht"
    assert data["status"] == "open"
    assert "id" in data


def test_get_created_ticket():
    post_response = client.post(
        "/tickets",
        json={"title": "Rechnung fehlt", "description": "Keine Mail erhalten"},
    )
    assert post_response.status_code == 201
    created = post_response.json()

    response = client.get(f"/tickets/{created['id']}")
    assert response.status_code == 200
    assert response.json() == created


def test_get_missing_ticket_returns_404():
    response = client.get("/tickets/99999")
    assert response.status_code == 404
