from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr
from typing import Union

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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
