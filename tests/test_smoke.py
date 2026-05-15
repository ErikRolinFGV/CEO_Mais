"""Smoke test mínimo para validar que o app sobe."""

from fastapi.testclient import TestClient


def test_health_endpoint() -> None:
    """O endpoint raiz deve responder com status ok."""
    # Import dentro da função para evitar erro caso .env ainda não esteja configurado
    from app.main import app

    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
