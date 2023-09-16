import pytest

from catfishio.api.chat.mappers import event_handler_dict_to_model
from catfishio.api.chat.models import (
    ChatMessageResponse,
    ChatResizeResponse,
    MousePositionResponse,
    Position,
    TypesEnum,
)


def test_event_handler_dict_to_model_returns_mouse_position_response():
    event_handler_dict = {
        "type": TypesEnum.MOUSE_POSITION,
        "x": "0px",
        "y": "0px",
        "font_size": "20px",
        "emoji": "🎈",
    }
    expected = MousePositionResponse(
        type=TypesEnum.MOUSE_POSITION,
        username="test",
        position=Position(x=0, y=0, font_size=20),
        emoji="🎈",
    )
    actual = event_handler_dict_to_model("test", event_handler_dict)
    assert actual == expected


def test_event_handler_dict_to_model_returns_chat_message_response():
    event_handler_dict = {"type": TypesEnum.CHAT_MESSAGE, "message": "test"}
    expected = ChatMessageResponse(type=TypesEnum.CHAT_MESSAGE, message="test", username="test")
    actual = event_handler_dict_to_model("test", event_handler_dict)
    assert actual == expected


def test_event_handler_dict_to_model_returns_chat_resize_response():
    event_handler_dict = {"type": TypesEnum.CHAT_RESIZE, "width": 0, "height": 0}
    expected = ChatResizeResponse(type=TypesEnum.CHAT_RESIZE, username="test", width=0, height=0)
    actual = event_handler_dict_to_model("test", event_handler_dict)
    assert actual == expected


def test_event_handler_dict_to_model_raises_value_error():
    event_handler_dict = {"type": "invalid", "message": "test"}
    with pytest.raises(ValueError):
        event_handler_dict_to_model("test", event_handler_dict)
