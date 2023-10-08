from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

from common.config import conf_dict
from common.consts import EXCEPT_PATH_LIST, EXCEPT_PATH_REGEX
from router import index, auth
from event import app_handler
from middlewares.trusted_hosts import TrustedHostMiddleware
from middlewares.token_validator import AccessControl

import uvicorn


def create_main() -> FastAPI:
    app = FastAPI()

    # add router
    app.include_router(index.router)
    app.include_router(auth.router)

    # add app event
    app.add_event_handler("startup", app_handler.startup)
    app.add_event_handler("shutdown", app_handler.shutdown)

    # add middleware
    app.add_middleware(
        AccessControl,
        except_path_list=EXCEPT_PATH_LIST,
        except_path_regex=EXCEPT_PATH_REGEX,
    )
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


app = create_main()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
