from fastapi import FastAPI

from router import index, auth
from event import app_handler

import uvicorn


def create_main() -> FastAPI:
    app = FastAPI()

    # add router
    app.include_router(index.router)
    app.include_router(auth.router)

    # add app event
    app.add_event_handler("startup", app_handler.startup)
    app.add_event_handler("shutdown", app_handler.shutdown)

    return app


app = create_main()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
