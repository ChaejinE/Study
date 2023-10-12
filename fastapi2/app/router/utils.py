from database.schema.users import User

from model.users import UserToken
from common.consts import JWT_SECRET, JWT_ALGORITHM

import jwt


async def is_email_exist(email: str) -> bool:
    get_email = await User.get(email=email)

    return True if get_email else False


def create_jwt_token(user_obj: User) -> dict:
    token = UserToken.model_validate(user_obj, from_attributes=True).model_dump()
    token = jwt.encode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token


def return_auth_token(jwt_token: str) -> dict:
    return dict(Authorization=f"Bearer {jwt_token}")
