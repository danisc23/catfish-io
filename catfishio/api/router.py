from fastapi import APIRouter

from catfishio.api.chat import router as chat_router

router = APIRouter()

router.include_router(chat_router.router)
