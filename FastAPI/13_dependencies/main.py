from typing import Annotated, Union
from fastapi import Depends, FastAPI, Cookie

app = FastAPI()


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    """
    We can declare dependency functions with async or syn path operation function
    Dependecy functions are just path operation functino withou path decorator
    It just "inject"s result to path operation function that has a dependecy with this

    Args:
        q (Union[str, None], optional): _description_. Defaults to None.
        skip (int, optional): _description_. Defaults to 0.
        limit (int, optional): _description_. Defaults to 100.

    Returns:
        _type_: _description_
    """
    return {"q": q, "skip": skip, "limit": limit}


# Depends class has a single parameter like a function
# We just declare as a parameter, not directly call it
# common_parameters(Depends) function can take parameters in the same way that path operation functions do
# FastAPI takes care of
## 1. Calling our dependecy function with correct parameters
## 2. Get the result from our function
## 3. Assign that result to the parameters in our path operation function
# We can write the shared code !
# FastAPI serves ours simple and intitutive way that makes plugins, depency injection

# Use Annotated because we can avoid tiny a duplicate code like a Depends(dependency function)
# We can use like type alias thanks to Annotated on the FastAPI
CommonsDep = Annotated[dict, Depends(common_parameters)]


@app.get("/items/")
async def read_items(commons: CommonsDep):
    return commons


@app.get("/users/")
async def read_users(commons: CommonsDep):
    return commons


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# Dependency should be just Callable like function, class ...
class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends()]):
    """
    We can declare Dependency class to above parameter, not Annotated[CommonQueryParams, Depends(CommonQueryParams)]
    FastAPI create CommonQueryParamas(Dependency) Instance for using dependecy, so we don't need to write full context (type, Depends(class))

    Args:
        commons (Annotated[CommonQueryParams, Depends): _description_

    Returns:
        _type_: _description_
    """
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response


# We can use sub-dependecy
def query_extractor(q: Union[str, None] = None):
    return q


def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[Union[str, None], Cookie()] = None,
):
    if not q:
        return last_query
    return q


@app.get("/item/")
async def read_query(
    query_or_default: Annotated[
        str, Depends(query_or_cookie_extractor, use_cache=False)
    ]
):
    """
    We can get query through query_extractor but if there are not query, we can get query throguh query_or_cookie_extractor, which is saved cookie before

    If you call mulitple times dependecy, you can get cached result
    If you dont wanna it, you can set use_cache to False

    Args:
        query_or_default (Annotated[str, Depends): _description_

    Returns:
        _type_: _description_
    """
    return {"q_or_cookie": query_or_default}


from fastapi.exceptions import HTTPException
from fastapi import Header


# If we don't need to return or use value in dependecies
# we could use dependencies parameters on a path operation decorator as Dpends list
# It just operate as normal dependecy, just not return value
async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


# app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])
## We can use dependencies globally


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]


"""
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
- We can use yield for extra steps after finishing
- try -> pass to path operation and finished -> finally

async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()


async def dependency_b(dep_a: Annotated[DepA, Depends(dependency_a)]):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)


async def dependency_c(dep_b: Annotated[DepB, Depends(dependency_b)]):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)
        
- FastAPI operates contextlib internally, so this is run in the corret order

more detail : https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#a-database-dependency-with-yield
- we need to read this docs for understanding dependecies with yield
"""


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
