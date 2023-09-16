import json

from fastapi import HTTPException, Request, WebSocket, WebSocketException, status

from catfishio.core.auth.models import User


async def get_logged_user(request: Request):
    user = request.headers.get("X-User")
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return User(**json.loads(user))


async def get_logged_user_for_websocket(websocket: WebSocket):
    user = websocket.headers.get("X-User")
    if user is None:
        await websocket.close()
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    return User(**json.loads(user))


async def logout_user(user_id: str):
    pass


async def login_user(request: Request):
    user_dict = {
        "display_name": request.headers.get("X-Display-Name"),
    }
    return User(**user_dict)
