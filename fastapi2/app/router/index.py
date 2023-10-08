from fastapi import APIRouter

from starlette.responses import Response
from starlette.requests import Request

from datetime import datetime

router = APIRouter()


@router.get("/")
async def index():
    current_time = datetime.utcnow()
    return Response(f"UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")


@router.get("/test")
async def test(request: Request):
    print("state.user", request.state.user)

    current_time = datetime.utcnow()
    return Response(
        f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})"
    )
