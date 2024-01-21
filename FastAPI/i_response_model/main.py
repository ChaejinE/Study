from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Union, Any

app = FastAPI()

"""
We can set return type as with input type
FastAPI will use this return type to
- Validate the returned data
- Add a JSON Schema for the response, in the OpenAPI path operation
- It will limit and filter the output data to what is defined in the return type
    - This is particularly important for security
"""


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
