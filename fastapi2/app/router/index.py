from fastapi import APIRouter, Depends
from starlette.responses import Response

from sqlalchemy.ext.asyncio import AsyncSession

from database.schema.users import User
from database.conn import get_async_session

from datetime import datetime

router = APIRouter()


@router.get("/")
async def index(session: AsyncSession = Depends(get_async_session)):
    current_time = datetime.utcnow()
    return Response(f"UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")
