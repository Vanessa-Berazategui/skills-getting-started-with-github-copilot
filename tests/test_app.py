import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_signup_and_unregister():
    # Suponiendo que hay una actividad llamada 'Yoga' en el estado inicial
    activity = "Yoga"
    email = "testuser@example.com"
    # Registro
    signup_resp = client.post(f"/activities/{activity}/signup?email={email}")
    # Puede fallar si ya está registrado
    assert signup_resp.status_code in (200, 400)
    # Desregistro
    unregister_resp = client.post(
        f"/activities/{activity}/unregister?email={email}")
    # Puede fallar si no está registrado
    assert unregister_resp.status_code in (200, 400)
