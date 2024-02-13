from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Union

app = FastAPI()
"""
OAuth2 was designed so that the backend or API could be independent of server that autenticate he user
But FastAPI Application will handle the API and authenticatation. it is "password flow" that is one of many OAuth2 ways
1. Send username, password in Frontend
2. Check username, password and Response with token that will be expired after some time in API
3. Save temporarily token in Frontend and user is moved other section. Front end also need to fecth some more data from API
so that token will be used for authorization (Bearer <token>)
"""

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    oauth2_scheme is a Callable, so we can use Depends
    It is used in the OpenAPI Schema, using FastAPI's security schema
    FastAPI knows that oauth2_scheme is OAuth2PasswordBearer Class to define security schema

    This API is will check Heater Authorization if Bearer value is exist or not
    and return header value(token) as string and if it is not exist, it will be retuend as 401 status
    So, we don't need to check Header

    Args:
        token (Annotated[str, Depends): _description_

    Returns:
        _type_: _description_
    """
    return {"token": token}


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
