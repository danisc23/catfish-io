import logging

from fastapi import WebSocket, WebSocketDisconnect

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConnectionManager:
    def __init__(self):
        self.connections: dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.connections[username] = websocket

    async def disconnect(self, username: str):
        try:
            del self.connections[username]
        except KeyError:
            pass

    async def send_personal_message(self, response: dict, username: str):
        await self.connections[username].send_text(response)

    async def broadcast(self, response: dict):
        disconnect_users = []
        for username, connection in self.connections.items():
            try:
                await connection.send_json(response)
            except WebSocketDisconnect as err:
                logger.error(err)
                disconnect_users.append(username)

        for username in disconnect_users:
            await self.disconnect(username)
