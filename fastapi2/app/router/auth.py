from fastapi import APIRouter, Depends

from starlette.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from common.consts import JWT_SECRET, JWT_ALGORITHM
from database.conn import get_async_session
from database.schema.users import User
from model.users import SnsType, Token, UserToken, UserRegister
from router.utils import is_email_exist

import bcrypt
import jwt

router = APIRouter(prefix="/auth")


@router.post("/register/{sns_type}", status_code=201, response_model=Token)
async def register(
    sns_type: SnsType,
    reg_info: UserRegister,
    session: AsyncSession = Depends(get_async_session),
):
    if sns_type == SnsType.email:
        get_email = await User.get(email=reg_info.email)
        is_exist = True if get_email else False
        if not reg_info.email or not reg_info.pw:
            return JSONResponse(
                status_code=400, content=dict(msg="Email and PW must be provided'")
            )
        if is_exist:
            return JSONResponse(status_code=400, content=dict(msg="EMAIL_EXIST"))

        hash_pw = bcrypt.hashpw(reg_info.pw.encode("utf-8"), bcrypt.gensalt())
        hash_pw = hash_pw.decode("utf-8")

        new_user = await User.create(
            session, auto_commit=True, pw=hash_pw, email=reg_info.email
        )
        token = UserToken.model_validate(new_user, from_attributes=True).model_dump()
        token = jwt.encode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        token = dict(Authorization=f"Bearer {token}")
        return token
    return JSONResponse(status_code=400, content=dict(msg="NOT_SUPPORTED"))
