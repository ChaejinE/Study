from typing import Dict

from fastapi import FastAPI

app = FastAPI()


# item_id will be passed to my function as the argument like "http://localhost:8000/items/foo"
@app.get("/items/{item_id}")
async def read_item(item_id) -> Dict:
    return {"item_id": item_id}


# item_id will be passed to my function as the argument like "http://localhost:8000/items/3"
# This API Function attached integer type runs data conversion, Not string "3" integer 3
# So, FastAPI gives me automatic rquest parsing
@app.get("/items/{item_id}")
async def read_item_int(item_id: int) -> Dict:
    """
    If you call "http://localhost:8000/items/foo" after remove above function hasn't type
    you would get error like below it
    {
    "detail": [
        {
        "type": "int_parsing",
        "loc": [
            "path",
            "item_id"
        ],
        "msg": "Input should be a valid integer, unable to parse string as an integer",
        "input": "foo",
        "url": "https://errors.pydantic.dev/2.1/v/int_parsing"
        }
    ]
    }
    This is Data Validation
    All the data validation is performed by Pydantic

    Args:
        item_id (int): Path Parameter

    Returns:
        Dict: _description_
    """
    return {"item_id": item_id}


# Order Matter
# user me calls this function not next function
# It is important waht we know that api is called first order
# If you wanna path parameter to be predefined, you can use Enum Class
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName) -> Dict:
    """

    Args:
        model_name (ModelName): We can check awsome selections in the docs

    Returns:
        Dict: _description_
    """
    message = ""

    # Python Enumerations
    if model_name is ModelName.alexnet:
        message = "Deep Learning FTW!"
    # Python str
    elif model_name.value == "lenet":
        message = "LeCNN all the images"

    return {"model_name": model_name, "message": message}


# Open API doesn't support path argument in the path parameter
# FastAPI supports it using internal execution, starlette
@app.get("/files/{file_path:path}")
async def read_file(file_path: str) -> Dict:
    """

    Args:
        file_path (str): Path Parameter
            We can use a url using ":path"

    Returns:
        Dict: _description_
    """
    return {"file_path": file_path}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
