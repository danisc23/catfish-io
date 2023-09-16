from enum import Enum

from pydantic import BaseModel, validator


class TypesEnum(str, Enum):
    """Enum for the different types of messages that can be sent over the WebSocket."""

    MOUSE_POSITION = "mouse-position"
    CHAT_MESSAGE = "chat-message"
    CHAT_RESIZE = "chat-resize"


class EventHandlerResponse(BaseModel):
    """Base class for all WebSocket responses that are sent to the client."""

    type: TypesEnum
    username: str

    @validator("username", allow_reuse=True, check_fields=False)
    def username_must_be_valid(cls, v):
        if len(v) > 60 or len(v) < 3:
            raise ValueError("username must be between 3 and 60 characters")
        return v


class Position(BaseModel):
    """Class for the mouse position."""

    x: int
    y: int
    font_size: int

    @validator("x")
    def x_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("x must be positive")
        return v

    @validator("y")
    def y_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("y must be positive")
        return v

    @validator("font_size")
    def font_size_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("font_size must be positive")
        return v


class MousePositionResponse(EventHandlerResponse):
    """WebSocket message received from the client when the user moves their mouse."""

    position: Position
    emoji: str

    @validator("emoji")
    def emoji_must_be_valid(cls, v):
        if len(v) != 1:
            raise ValueError("emoji must be a single character")
        return v

    @validator("type")
    def type_must_be_mouse_position(cls, v):
        if v != TypesEnum.MOUSE_POSITION:
            raise ValueError("type must be mouse-position")
        return v


class ChatMessageResponse(EventHandlerResponse):
    """WebSocket message received from the client when the user sends a chat message."""

    message: str

    @validator("message")
    def message_must_be_valid(cls, v):
        if len(v) > 255:
            raise ValueError("message must be less than 255 characters")
        return v

    @validator("type")
    def type_must_be_chat_message(cls, v):
        if v != TypesEnum.CHAT_MESSAGE:
            raise ValueError("type must be chat-message")
        return v


class ChatResizeResponse(EventHandlerResponse):
    """WebSocket message received from the client when the user resizes the chat window."""

    width: int
    height: int

    @validator("width")
    def width_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("width must be positive")
        return v

    @validator("height")
    def height_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("height must be positive")
        return v

    @validator("type")
    def type_must_be_chat_resize(cls, v):
        if v != TypesEnum.CHAT_RESIZE:
            raise ValueError("type must be chat-resize")
        return v


class MousePositionPayload(BaseModel):
    type: TypesEnum
    emoji: str
    x: str
    y: str
    font_size: str

    @validator("type")
    def type_must_be_mouse_position(cls, v):
        if v != TypesEnum.MOUSE_POSITION:
            raise ValueError("type must be mouse-position")
        return v

    @validator("emoji")
    def emoji_must_be_valid(cls, v):
        if len(v) != 1:
            raise ValueError("emoji must be a single character")
        return v

    @classmethod
    def contains_px_and_could_be_int(cls, value: str) -> bool:
        return value.endswith("px") and value.replace("px", "").isdigit()

    @validator("x")
    def x_must_be_valid(cls, v):
        if not cls.contains_px_and_could_be_int(v):
            raise ValueError("x must be a valid integer with px")
        return v

    @validator("y")
    def y_must_be_valid(cls, v):
        if not cls.contains_px_and_could_be_int(v):
            raise ValueError("y must be a valid integer with px")
        return v

    @validator("font_size")
    def font_size_must_be_valid(cls, v):
        if not cls.contains_px_and_could_be_int(v):
            raise ValueError("font_size must be a valid integer with px")
        return v
