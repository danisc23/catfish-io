from catfishio.api.chat.models import (
    ChatMessageResponse,
    ChatResizeResponse,
    EventHandlerResponse,
    MousePositionPayload,
    MousePositionResponse,
    TypesEnum,
)


def event_handler_dict_to_model(username: str, event_handler_dict: dict) -> EventHandlerResponse:
    event_handler_dict["username"] = username
    if event_handler_dict.get("type") == TypesEnum.MOUSE_POSITION:
        payload = MousePositionPayload.parse_obj(event_handler_dict)
        event_handler_dict["position"] = {
            "x": payload.x.replace("px", ""),
            "y": payload.y.replace("px", ""),
            "font_size": payload.font_size.replace("px", ""),
        }
        return MousePositionResponse.parse_obj(event_handler_dict)
    elif event_handler_dict.get("type") == TypesEnum.CHAT_MESSAGE:
        return ChatMessageResponse.parse_obj(event_handler_dict)
    elif event_handler_dict.get("type") == TypesEnum.CHAT_RESIZE:
        return ChatResizeResponse.parse_obj(event_handler_dict)
    else:
        raise ValueError(f"Invalid type: {event_handler_dict.get('type')}")
