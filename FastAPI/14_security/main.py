from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
