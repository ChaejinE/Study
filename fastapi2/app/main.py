from fastapi import FastAPI, Depends
from fastapi.security import APIKeyHeader

from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from common.config import conf_dict
from router import index, auth, users
from event import app_handler
from middlewares.trusted_hosts import TrustedHostMiddleware
from middlewares.token_validator import access_control

import uvicorn

API_KEY_HEADER = APIKeyHeader(name="Authorization", auto_error=False)


def create_app() -> FastAPI:
    app = FastAPI()

    # add router
    app.include_router(index.router)
    app.include_router(auth.router, prefix="/api")
    app.include_router(
        users.router, prefix="/api", dependencies=[Depends(API_KEY_HEADER)]
    )

    # add app event
    app.add_event_handler("startup", app_handler.startup)
    app.add_event_handler("shutdown", app_handler.shutdown)

    # add middleware
    """
    프로그램은 스택구조이므로 TrustedhostMiddleware -> CORS -> AccessControl 순으로 동작한다.
    """
    app.add_middleware(BaseHTTPMiddleware, dispatch=access_control)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=conf_dict["ALLOW_SITE"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=conf_dict["TRUSTED_HOSTS"],
        except_path=["/health"],
    )

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
