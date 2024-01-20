from fastapi import FastAPI
from typing import Dict

app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# If you declare other fucntion parameters that are not part of the path parameters
# they are automatically interpreted as query parameters
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10) -> Dict:
    """
    http://127.0.0.1:8000/items/
    == (Same)
    http://127.0.0.1:8000/items/?skip=0&limit=10

    http://127.0.0.1:8000/items/?skip=20
    - skip = 20
    - limit = 10 (default value)

    It is adapted automatically Data Validation if you above set type part of the quert parameters
    Bool type is All True value otheriwse as False value

    If you don't set default value part of query param
    It will be required. you have to pass query value for avoding api error

    Args:
        skip (int, optional): _description_. Defaults to 0.
        limit (int, optional): _description_. Defaults to 10.

    Returns:
        _type_: _description_
    """
    return fake_items_db[skip : skip + limit]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
