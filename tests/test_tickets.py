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


def test_create_ticket_keeps_priority():
    response = client.post(
        "/tickets",
        json={"title": "Server down", "description": "Alles tot", "priority": "high"},
    )
    assert response.status_code == 201
    assert response.json()["priority"] == "high"


def test_create_ticket_rejects_blank_description():
    response = client.post(
        "/tickets",
        json={"title": "Login geht nicht", "description": "   "},
    )
    assert response.status_code == 422


def test_filter_by_status_open():
    client.post("/tickets", json={"title": "Filter Test", "description": "x"})
    response = client.get("/tickets", params={"status": "open"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert all(t["status"] == "open" for t in data)
