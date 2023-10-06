# from fastapi import APIRouter, Depends
# from starlette.responses import Response

# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select

# from database.schema import User
# from main import get_session

# from datetime import datetime

# router = APIRouter()


# @router.get("/")
# async def index(session: AsyncSession = Depends(get_session)):
#     User().create(session, auto_commit=True, name="코알라")
#     current_time = datetime.utcnow()
#     return Response(f"UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")
