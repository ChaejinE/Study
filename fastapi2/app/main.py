from fastapi import FastAPI
from router import index

import uvicorn


def create_main() -> FastAPI:
    app = FastAPI()

    app.include_router(index.router)

    return app


app = create_main()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
