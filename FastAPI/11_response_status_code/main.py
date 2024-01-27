from fastapi import FastAPI, status, HTTPException

app = FastAPI()

"""
100 : Information, This response isn't included Body
200 : Successful, Everything is good
- 201 : Create Success
- 204 : No Content, This response isn't included Body
300 : Redirection, This response might be included Body
- 304 : Not Modified, This response isn't included Body
400 : Client Error
500 : Server Error
"""


# We can use the convenience varibale from fastapi.status
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}


items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    """
    We can raise error when it is problems like access permission, wrong request, etc

    Args:
        item_id (str): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    if item_id not in items:
        # We can set custom headers in the Exception for advanced scenario
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}


# We can make custom Exception
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


from fastapi import Request
from fastapi.responses import JSONResponse


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder


# We can also override exception handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
        It will add more infromation, which is body using exec.body

        {
      "detail": [
        {
          "loc": [
            "body",
            "size"
          ],
          "msg": "value is not a valid integer",
          "type": "type_error.integer"
        }
      ],
      "body": {
        "title": "towel",
        "size": "XL"
      }
    }

        Args:
            request (Request): _description_
            exc (RequestValidationError): _description_

        Returns:
            _type_: _description_
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


from pydantic import BaseModel


class Item(BaseModel):
    title: str
    size: int


@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
