from fastapi import APIRouter, Depends
from starlette.responses import Response

from sqlalchemy.ext.asyncio import AsyncSession

from database.schema import User
from database.conn import get_db

from datetime import datetime

router = APIRouter()


@router.get("/")
async def index(session: AsyncSession = Depends(get_db)):
    user = User()
    user.name = "코알라"
    session.add(user)
    await session.commit()
    await session.refresh(user)
    current_time = datetime.utcnow()
    return Response(f"UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")
