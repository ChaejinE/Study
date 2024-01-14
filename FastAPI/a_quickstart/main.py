from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


"""
HTTP GET APIs
"""

@app.get("/")
async def read_root() -> dict:
    """
    http://127.0.0.1:8000/
    
    Returns:
        dict: {"Hello":"World"}
    """
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None) -> dict:
    """
    It is prceesed through below stages
    
    1. Validation existing item_id in GET/PUT request's path
    2. Validation type item_id whether or not integer
    3. Check if there is an optional query parameters q
        - it is required if q is not None
    4. 
    Args:
        item_id (int): Path Parameter 
        q (Union[str, None], optional): Query Parameter. Defaults to None.

    Returns:
        dict: {"item_id":5,"q":"somequery"}
    """
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item) -> dict:
    """
    http://127.0.0.1:8000/docs
    Try update API and check Request body
    It is awsome there is Item Class's memeber variabels
    
    For this PUT request, read the body as JSON
    - 1. Check name that should be a str
    - 2. Check price that should be a float
    - 3. Check is_offer that shouild be a bool, if present
    - It is converted from and to JSON automatically
    - It is also used by Interative docs systems and automatic client code generation system. (OpenAPI etc)
    
    Args:
        item_id (int): Path Parameter
        item (Item): name, price, is_offer
            We can get below things
            - Data Validation (JSON, Format error etc..)
            - Data Transformation (type, parameters forms, file database_model etc...)
            - Swagger, Redoc
            

    Returns:
        dict: {"item_name": item.name, "item_id": item_id}
    """
    return {"item_name": item.name, "item_id": item_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port = 8000, reload=True)
