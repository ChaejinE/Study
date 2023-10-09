from fastapi import APIRouter

from starlette.requests import Request

from database.schema.users import User
from model.users import UserMe

router = APIRouter()


@router.get("/me", response_model=UserMe)
async def get_user(request: Request):
    user = request.state.user
    user_info = User.get(id=user.id)

    return user_info
