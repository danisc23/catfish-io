import pytest
from fastapi.testclient import TestClient

from catfishio.main import app


@pytest.fixture(name="client")
def fixture_client():
    return TestClient(app)


def test_event_handler_chat_message(client):
    with client.websocket_connect("/api/ws/event-handler/test") as websocket:
        message = {"type": "chat-message", "message": "Hello World!"}
        websocket.send_json(message)
        data = websocket.receive_json()
        assert data == {
            "type": "chat-message",
            "message": "Hello World!",
            "username": "test",
        }


def test_event_handler_mouse_position(client):
    with client.websocket_connect("/api/ws/event-handler/test") as websocket:
        message = {
            "type": "mouse-position",
            "x": "0px",
            "y": "0px",
            "font_size": "20px",
            "emoji": "🎈",
        }
        websocket.send_json(message)
        data = websocket.receive_json()
        assert data == {
            "type": "mouse-position",
            "username": "test",
            "position": {"x": 0, "y": 0, "font_size": 20},
            "emoji": "🎈",
        }


def test_event_handler_chat_resize(client):
    with client.websocket_connect("/api/ws/event-handler/test") as websocket:
        message = {"type": "chat-resize", "width": 0, "height": 0}
        websocket.send_json(message)
        data = websocket.receive_json()
        assert data == {
            "type": "chat-resize",
            "username": "test",
            "width": 0,
            "height": 0,
        }


def test_event_handler_invalid_message(client):
    with client.websocket_connect("/api/ws/event-handler/test") as websocket:
        message = {
            "type": "invalid-message",
            "username": "test",
            "message": "Hello World!",
        }
        websocket.send_json(message)
        with pytest.raises(ValueError):
            websocket.receive_json()
