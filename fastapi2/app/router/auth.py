from fastapi import APIRouter, Depends

from starlette.responses import JSONResponse

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.conn import get_async_session
from database.schema.users import User
from model.users import SnsType, Token, UserRegister
from router.utils import is_email_exist, create_jwt_token, return_auth_token

import bcrypt

router = APIRouter(prefix="/auth")


@router.post("/register/{sns_type}", status_code=201, response_model=Token)
async def register(
    sns_type: SnsType,
    reg_info: UserRegister,
    session: AsyncSession = Depends(get_async_session),
):
    if sns_type == SnsType.email:
        is_exist = await is_email_exist(email=reg_info.email)
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
        token = await create_jwt_token(new_user)
        token = await return_auth_token(token)
        return token
    return JSONResponse(status_code=400, content=dict(msg="NOT_SUPPORTED"))


@router.post("/login/{sns_type}", status_code=200, response_model=Token)
async def login(
    sns_type: SnsType,
    user_info: UserRegister,
    session: AsyncSession = Depends(get_async_session),
):
    if sns_type == SnsType.email:
        if not user_info.email or not user_info.pw:
            return JSONResponse(
                status_code=400, content=dict(msg="Email and PW must be provided")
            )
        query = select(User).limit(10)
        check_dict = {"email": user_info.email}
        for key, val in check_dict.items():
            col = getattr(User, key)
            query = query.filter(col == val)
        user = None
        query_result = await session.execute(query)
        user = query_result.scalars().first()
        if not user:
            return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_USER"))

        is_verified = bcrypt.checkpw(
            user_info.pw.encode("utf-8"), user.pw.encode("utf-8")
        )
        if not is_verified:
            return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_USER"))

        token = create_jwt_token(user)
        token = return_auth_token(token)
        return token
    return JSONResponse(status_code=400, content=dict(msg="NOT_SUPPORTED"))
