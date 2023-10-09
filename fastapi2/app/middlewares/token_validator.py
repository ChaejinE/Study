from starlette.types import ASGIApp, Scope, Receive, Send
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.datastructures import Headers

from common import consts
from exception import api as apiEx
from model.users import UserToken
from middlewares.utils import D

import typing
import time
import re
import jwt


class AccessControl:
    def __init__(
        self,
        app: ASGIApp,
        except_path_list: typing.Sequence[str] = None,
        except_path_regex: str = None,
    ) -> None:
        if except_path_list is None:
            except_path_list = ["*"]

        self._app = app
        self._except_path_list = except_path_list
        self._except_path_regex = except_path_regex

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        request = Request(scope=scope)
        headers = Headers(scope=scope)
        print(f"request: {request}, headers: {headers}")

        request.state.start = time.time()
        request.state.inpect = None  # Recommand Sentry
        request.state.user = None
        request.state.is_admin_access = None
        # AWS, LoadBalancer
        # ip_from = (
        #     request.headers["x-forwarded-for"]
        #     if "x-forwarded-for" in request.headers.keys()
        #     else None
        # )

        if (
            await self.url_pattern_check(request.url.path, self._except_path_regex)
            or request.url.path in self._except_path_list
        ):
            await self._app(scope, receive, send)

        try:
            if request.url.path.startswith("/api"):
                if "Authorization" in request.headers.keys():
                    token_info = await self.token_decode(
                        request.headers.get("Authorization")
                    )
                    request.state.user = UserToken(**token_info)
                    # Token 없음
                elif "Authorization" not in request.headers.keys():
                    raise apiEx.NotAuthorized()
            else:
                # api가 아니라 template 요청 (Server side job) 인 경우
                print("내가만든쿠키: ", request.cookies)
                # request.cookies["Authorization"] = "Bearer "

                if "Authorization" not in request.cookies.keys():
                    raise apiEx.NotAuthorized()

                token_info = await self.token_decode(
                    access_token=request.cookies.get("Authorization")
                )
                request.state.user = UserToken(**token_info)

            request.state.req_time = D.datetime()
            res = await self._app(scope, receive, send)

        except apiEx.APIException as e:
            res = await self.exception_handler(e)
            res = await res(scope, receive, send)

        return res

    @staticmethod
    async def url_pattern_check(path, pattern):
        result = re.match(pattern, path)
        if result:
            return True
        return False

    @staticmethod
    async def token_decode(access_token):
        try:
            access_token = access_token.replace("Bearer ", "")
            payload = jwt.decode(
                access_token, key=consts.JWT_SECRET, algorithms=[consts.JWT_ALGORITHM]
            )
        except jwt.PyJWTError as e:
            print(e)

        return payload

    @staticmethod
    async def exception_handler(error: apiEx.APIException):
        error_dict = dict(
            status=error.status_code,
            msg=error.msg,
            detail=error.detail,
            code=error.code,
        )
        res = JSONResponse(status_code=error.status_code, content=error_dict)
        return res
