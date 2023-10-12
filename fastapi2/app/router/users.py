from fastapi import APIRouter, Depends

from starlette.requests import Request
from starlette.responses import Response

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.conn import get_async_session
from database.schema.users import User
from model.users import UserMe

router = APIRouter()


@router.get("/me", response_model=UserMe)
async def get_user(
    request: Request, session: AsyncSession = Depends(get_async_session)
):
    user = request.state.user
    query = select(User).limit(10)
    col = getattr(User, "id")
    query = query.filter(col == user.id)
    query_result = await session.execute(query)
    user_info = query_result.scalars().all()
    if len(user_info) > 1:
        raise Exception("It must be only one user")
    elif user_info:
        user_info = UserMe.model_validate(
            user_info[0], from_attributes=True
        ).model_dump()
    else:
        return Response(status_code=400, content="User Not Found")

    return user_info
