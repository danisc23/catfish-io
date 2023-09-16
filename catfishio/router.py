from fastapi import APIRouter

from catfishio.api import router as api_router
from catfishio.web import router as web_router

router = APIRouter()

router.include_router(api_router.router, prefix="/api")
router.include_router(web_router.router, prefix="/web")
