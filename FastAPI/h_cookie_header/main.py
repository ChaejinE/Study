from fastapi import FastAPI, Cookie, Header
from typing import Annotated, Union, List

app = FastAPI()


# You could declare the cookie parameters using same structure as with Path and Query
@app.get("/items")
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id": ads_id}


# Yoy could also declare the hader parameters like above that
# Header has a little extra functinality on top of what Path, Query and Cookie provide
# HTTP headers has '-', but it is not python style. So fastapi converts from '_' to '-'
# It might be raised erorr at a few case. so we can tranfer parameter, convert_underscores=False
@app.get("/header/items")
async def read_items(
    user_agent: Annotated[Union[str, None], Header()] = None,
    strange_header: Annotated[
        Union[str, None], Header(convert_underscores=False)
    ] = None,
):
    return {"User-Agent": user_agent, "strange_header": strange_header}


# It is possible to receive duplicate headers
@app.get("/duplicated/hedaer/items/")
async def read_items(x_token: Annotated[Union[List[str], None], Header()] = None):
    return {"X-Token values": x_token}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
