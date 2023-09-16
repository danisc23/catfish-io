import logging

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()
templates = Jinja2Templates(directory="catfishio/web/templates")


@router.get(
    "/chat/{username}",
    response_class=HTMLResponse,
)
async def get_chat(request: Request, username: str):
    logger.info(f"User: {username}")
    return templates.TemplateResponse("index.html", {"request": request, "username": username})
