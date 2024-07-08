from starlette.testclient import TestClient

from app.main_websocket import app


def test_read_main():
    client = TestClient(app)
    response = client.get("/main_websocket")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_websocket():
    client = TestClient(app)
    with client.websocket_connect("/test_ws") as websocket:
        data = websocket.receive_json()
        assert data == {"msg": "Hello WebSocket"}
