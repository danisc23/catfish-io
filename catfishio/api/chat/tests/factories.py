from pydantic_factories import ModelFactory

from catfishio.api.chat.models import (
    ChatMessageResponse,
    ChatResizeResponse,
    EventHandlerResponse,
    MousePositionPayload,
    MousePositionResponse,
    Position,
    TypesEnum,
)


class PositionFactory(ModelFactory):
    __model__ = Position


class EventHandlerResponseFactory(ModelFactory):
    __model__ = EventHandlerResponse

    username = "factory_user"


class MousePositionResponseFactory(EventHandlerResponseFactory):
    __model__ = MousePositionResponse

    type = TypesEnum.MOUSE_POSITION
    emoji = "🎈"


class ChatMessageResponseFactory(EventHandlerResponseFactory):
    __model__ = ChatMessageResponse

    type = TypesEnum.CHAT_MESSAGE
    message = "factory_message"


class ChatResizeResponseFactory(EventHandlerResponseFactory):
    __model__ = ChatResizeResponse

    type = TypesEnum.CHAT_RESIZE


class MousePositionPayloadFactory(ModelFactory):
    __model__ = MousePositionPayload

    type = TypesEnum.MOUSE_POSITION
    emoji = "🎈"
    x = "0px"
    y = "0px"
    font_size = "20px"
