from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from catfishio.api.chat.mappers import event_handler_dict_to_model
from catfishio.core.managers.connection_manager import ConnectionManager

router = APIRouter()
manager = ConnectionManager()


@router.websocket("/ws/event-handler/{username}")
async def event_handler(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    while True:
        try:
            data = await websocket.receive_json()
        except WebSocketDisconnect:
            await manager.disconnect(username)
            break

        data = event_handler_dict_to_model(username, data)
        await manager.broadcast(data.dict())
