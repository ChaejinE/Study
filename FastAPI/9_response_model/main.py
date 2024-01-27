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


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(BaseModel):
    # It inhertis from BaseUser. so it will include all the fields from both models
    password: str


# Password is in a input, but is not in a output becuase of response_model
@app.post("/user/", response_model=BaseUser)
async def create_user(user: UserIn) -> Any:
    return user


from fastapi import Response
from fastapi.responses import JSONResponse, RedirectResponse


# We can return a response directly
# Responses is subclass of Response. so they are handled by fastapi
@app.post("/protal")
def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimentional protal"})


# Return type is invalid pydantic type so without reponse_model=None, it is fail
# So, add response_model=None
# It don't apply to valid data by pydantic
@app.post("/protal2", response_model=None)
def get_portal(teleport: bool = False) -> Union[Response, dict]:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


# If response_model_exclude_unset set True, it makes not pass default value
# We can use response_model_exclude, response_model_include
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
