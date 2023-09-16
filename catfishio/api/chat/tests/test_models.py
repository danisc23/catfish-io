import pytest

from catfishio.api.chat.models import TypesEnum
from catfishio.api.chat.tests.factories import (
    ChatMessageResponseFactory,
    ChatResizeResponseFactory,
    MousePositionPayloadFactory,
    MousePositionResponseFactory,
    PositionFactory,
)


def test_event_handler_inherits_validators():
    child_factories = [
        MousePositionResponseFactory,
        ChatMessageResponseFactory,
        ChatResizeResponseFactory,
    ]

    for factory in child_factories:
        with pytest.raises(ValueError):
            factory.build(username="a" * 100)

        with pytest.raises(ValueError):
            factory.build(username="a")


def test_position():
    position = PositionFactory.build()
    assert position.x >= 0
    assert position.y >= 0
    assert position.font_size >= 0


def test_postion_raises_value_error():
    with pytest.raises(ValueError):
        PositionFactory.build(x=-1)

    with pytest.raises(ValueError):
        PositionFactory.build(y=-1)

    with pytest.raises(ValueError):
        PositionFactory.build(font_size=-1)


def test_mouse_position():
    mouse_position = MousePositionResponseFactory.build()
    assert mouse_position.type == TypesEnum.MOUSE_POSITION
    assert mouse_position.username == "factory_user"
    assert mouse_position.position.x >= 0
    assert mouse_position.position.y >= 0
    assert mouse_position.position.font_size >= 0
    assert mouse_position.emoji == "🎈"


def test_mouse_position_raises_value_error():
    with pytest.raises(ValueError):
        MousePositionResponseFactory.build(emoji="🔪🎈🎇")

    with pytest.raises(ValueError):
        MousePositionResponseFactory.build(type=TypesEnum.CHAT_MESSAGE)


def test_chat_message():
    chat_message = ChatMessageResponseFactory.build()
    assert chat_message.type == TypesEnum.CHAT_MESSAGE
    assert chat_message.username == "factory_user"
    assert chat_message.message == "factory_message"


def test_chat_message_raises_value_error():
    with pytest.raises(ValueError):
        ChatMessageResponseFactory.build(type=TypesEnum.MOUSE_POSITION)

    with pytest.raises(ValueError):
        ChatMessageResponseFactory.build(message="a" * 256)


def test_chat_resize():
    chat_resize = ChatResizeResponseFactory.build(width=0, height=0)
    assert chat_resize.type == TypesEnum.CHAT_RESIZE
    assert chat_resize.username == "factory_user"
    assert chat_resize.width == 0
    assert chat_resize.height == 0


def test_chat_resize_raises_value_error():
    with pytest.raises(ValueError):
        ChatResizeResponseFactory.build(type=TypesEnum.MOUSE_POSITION)

    with pytest.raises(ValueError):
        ChatResizeResponseFactory.build(width=-1)

    with pytest.raises(ValueError):
        ChatResizeResponseFactory.build(height=-1)


def test_mouse_position_payload():
    mouse_position_payload = MousePositionPayloadFactory.build(
        x="1px",
        y="2px",
        font_size="20px",
    )
    assert mouse_position_payload.type == TypesEnum.MOUSE_POSITION
    assert mouse_position_payload.x == "1px"
    assert mouse_position_payload.y == "2px"
    assert mouse_position_payload.font_size == "20px"
    assert mouse_position_payload.emoji == "🎈"


def test_mouse_position_payload_raises_value_error():
    with pytest.raises(ValueError) as invalid_type:
        MousePositionPayloadFactory.build(type=TypesEnum.CHAT_MESSAGE)

    with pytest.raises(ValueError) as invalid_emoji:
        MousePositionPayloadFactory.build(emoji="🔪🎈🎇")

    with pytest.raises(ValueError) as invalid_x:
        MousePositionPayloadFactory.build(
            x="1ppx",
        )

    with pytest.raises(ValueError) as invalid_y:
        MousePositionPayloadFactory.build(y="px")

    with pytest.raises(ValueError) as invalid_font_size:
        MousePositionPayloadFactory.build(
            font_size="-20px",
        )

    assert "type must be mouse-position" in str(invalid_type.value)
    assert "emoji must be a single character" in str(invalid_emoji.value)
    for exception in [invalid_x, invalid_y, invalid_font_size]:
        assert "must be a valid integer with px" in str(exception.value)
