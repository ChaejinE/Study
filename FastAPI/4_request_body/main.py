"""
You need to send data from a client to your API
You can send it as a request body

Response Body is the data your API sends to the client

This time's main is learning pydantic's power
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    """
    If a model attribute has a default value, it is not required

    Args:
        BaseModel (_type_): _description_
    """

    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    """
    This model (Item) declares a JSON object (Python dict)

    Item is not requried description, tax. because it is set to optional
    So, Keywords, name and price, would be only validation

    Reulsts
    - Read the Bodu of the request as JSON
    - Convert the corresponding types
    - Validate the data
    - Generate JSON Schema
        - It will be part of the generated OpenAPI schema and automatic docs UIs
    - Editor support

    Args:
        item (Item): _description_

    Returns:
        _type_: _description_
    """
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
