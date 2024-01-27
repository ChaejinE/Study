from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


from fastapi import Body
from typing_extensions import Annotated


@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body(gt=0)]
):
    """
    For example, extending the previous model, you could decide that you want to have another key importance
    in the same body, besides the item and user
    You can instruct FastAPI to treat it as another body key using Body

    Args:
        item_id (int): _description_
        item (Item): _description_
        user (User): _description_
        importance (Annotated[int, Body): _description_

    Returns:
        _type_: _description_
    """
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


@app.put("/body/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    """
    Lets say, we have a single item body param from a Pydantic model.
    By default, FastAPI will then expect is body directly
    But if you want it to expect a JSON with a key, you can use the special Body Parameter embed
    If you don't declare Body embed True, item key would not be existed

    Args:
        item_id (int): _description_
        item (Annotated[Item, Body, optional): _description_. Defaults to True)].

    Returns:
        _type_: _description_
    """
    results = {"item_id": item_id, "item": item}
    return results


from pydantic import Field


class Item2(BaseModel):
    """
    Pydantic's Field is used to declare validation and metadata inside instead of Query, Path, Body
    It is not from fastapi as are Query, Path, Body and is imported directly
    It can declare more model's attributes as a Query, Path and Body, it's same
    Actually, Query, Path and Body Class is a subclass of FieldInfo Class so that Field is same structure with that

    Args:
        BaseModel (_type_): _description_
    """

    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


class Image(BaseModel):
    url: str
    name: str


class Item3(BaseModel):
    """
    This is nested model example
    We can use the submodel, Image, as a type
    like below

    {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2,
        "tags": ["rock", "metal", "bar"],
        "image": {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        }
    }


    Args:
        BaseModel (_type_): _description_
    """

    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()
    image: Union[Image, None] = None


from pydantic import HttpUrl


class Image2(BaseModel):
    """
    Reference : https://docs.pydantic.dev/latest/concepts/types/
    We can use special types and get validation
    HttpUrl will be checked to be a valid URL and documented in JSON Schema / OpenAPI

    It is also used as more deeply nested models

    Args:
        BaseModel (_type_): _description_
    """

    url: HttpUrl
    name: str


class Item4(BaseModel):
    """
    We can use list attribute

    {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2,
        "tags": [
            "rock",
            "metal",
            "bar"
        ],
        "images": [
            {
                "url": "http://example.com/baz.jpg",
                "name": "The Foo live"
            },
            {
                "url": "http://example.com/dave.jpg",
                "name": "The Baz"
            }
        ]
    }

    Args:
        BaseModel (_type_): _description_
    """

    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()
    images: Union[list[Image2], None] = None


@app.post("/images/multiple")
async def create_multiple_images(*, images: list[Image2]):
    for image in images:
        image.url
    return images


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    """
    You can declare a body as dict

    Args:
        weights (dict[int, float]): _description_

    Returns:
        _type_: _description_
    """
    return weights


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
