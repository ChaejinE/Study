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


from fastapi import Query
from typing_extensions import Annotated
from typing import Union, List

@app.get("/annotated/")
async def read_items(q: Annotated[Union[str, None], Query(max_length=50, pattern="^fixedquery$")] = None):
    """
    Additional validation
    It is provided, its length doesn't exceed 50 chracters
    
    Annotated can be used to add metadata to your parameters
    Having a Query(max_length=50), we are telling FastAPI that we want it to extract this value from the query parameters
    - Validate the data making sure that the max length is 50 chracaters
    - Show a clear error for the client when the data is not valid
    
    Using Annotated is recommended instad of the defulat value in function parameters
    
    We can also add regular expressions
    
    Above query parameter is not required
    If you change required, you can add Ellipsis(...) q: Annotated[Uni..] = ...
    It is used by Pydantic and FastAPI to explcitily declare that a value is required
    
    Args:
        q (Annotated[Union[str, None], Query, optional): _description_. Defaults to 50)]=None.

    Returns:
        _type_: _description_
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    
    return results

@app.get("/annotatedlist/")
async def read_items(q: Annotated[Union[List[str], None], Query()] = None):
    """
    We can declare query parameter for list / multiple values
    http://localhost:8003/annotatedlist/?q=foo&q=bar
    
    If you don't need to check list's element type, you can use just "Union[list, None]"
    
    Args:
        q (Annotated[Union[str, None], Query, optional): _description_. Defaults to 50)]=None.

    Returns:
        _type_: _description_
    """
    query_items = {"q": q}
    return query_items


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
