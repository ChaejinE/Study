from starlette.types import ASGIApp, Scope, Receive, Send
from starlette.requests import Request
from starlette.responses import JSONResponse

from common import consts
from exception import api as apiEx
from middlewares.utils import api_logger
from model.users import UserToken
from middlewares.utils import D

import time
import re
import jwt


async def access_control(request: Request, call_next) -> None:
    request.state.req_time = D.datetime()
    request.state.start = time.time()
    request.state.inspect = None  # Recommand Sentry
    request.state.user = None
    ip = (
        request.headers["x-forwarded-for"]
        if "x-forwarded-for" in request.headers.keys()
        else request.client.host
    )
    request.state.ip = ip.split(",")[0] if "," in ip else ip
    headers = request.headers
    cookies = request.cookies
    url = request.url.path

    # AWS, LoadBalancer
    # ip_from = (
    #     request.headers["x-forwarded-for"]
    #     if "x-forwarded-for" in request.headers.keys()
    #     else None
    # )

    if (
        await url_pattern_check(url, consts.EXCEPT_PATH_REGEX)
        or url in consts.EXCEPT_PATH_LIST
    ):
        response = await call_next(request)
        if url != "/":
            await api_logger(request=request, response=response)
        return response

    try:
        if url.startswith("/api"):
            if "Authorization" in headers.keys():
                token_info = await token_decode(headers.get("Authorization"))
                request.state.user = UserToken(**token_info)
                # Token 없음
            elif "Authorization" not in headers.keys():
                raise apiEx.NotAuthorized()
        else:
            # api가 아니라 template 요청 (Server side job) 인 경우
            print("내가만든쿠키: ", cookies)
            # request.cookies["Authorization"] = "Bearer "

            if "Authorization" not in cookies.keys():
                raise apiEx.NotAuthorized()

            token_info = await token_decode(access_token=cookies.get("Authorization"))
            request.state.user = UserToken(**token_info)

        response = await call_next(request)
        await api_logger(request=request, response=response)

    except apiEx.APIException as e:
        error = await exception_handler(e)
        error_dict = dict(
            status=error.status_code,
            msg=error.msg,
            detail=error.detail,
            code=error.code,
        )
        response = JSONResponse(status_code=error.status_code, content=error_dict)
        await api_logger(request=request, error=error)

    return response


async def url_pattern_check(path, pattern):
    result = re.match(pattern, path)
    if result:
        return True
    return False


async def token_decode(access_token):
    try:
        access_token = access_token.replace("Bearer ", "")
        payload = jwt.decode(
            access_token, key=consts.JWT_SECRET, algorithms=[consts.JWT_ALGORITHM]
        )
    except jwt.exceptions.ExpiredSignatureError:
        raise apiEx.TokenExpiredEx()
    except jwt.exceptions.DecodeError:
        raise apiEx.TokenDecodeEx()

    return payload


async def exception_handler(error: Exception):
    if not isinstance(error, apiEx.APIException):
        error = apiEx.APIException(ex=error, detail=str(error))
    return error
