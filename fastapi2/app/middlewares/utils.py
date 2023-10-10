from fastapi.logger import logger
from fastapi.requests import Request

from datetime import datetime, date, timedelta

import time
import json


class D:
    def __init__(self, *args):
        self.utc_now = datetime.utcnow()
        self.timedelta = 0

    @classmethod
    def datetime(cls, diff: int = 0) -> datetime:
        return (
            cls().utc_now + timedelta(hours=diff)
            if diff > 0
            else cls().utc_now + timedelta(hours=diff)
        )

    @classmethod
    def date(cls, diff: int = 0) -> date:
        return cls.datetime(diff=diff).date()

    @classmethod
    def date_num(cls, diff: int = 0) -> int:
        return int(cls.date(diff=diff).strftime("%Y%m%d"))


async def api_logger(request: Request, response=None, error=None):
    time_format = "%Y/%m/%d %H:%M:%S"
    t = time.time() - request.state.start
    status_code = error.status_code if error else response.status_code
    error_log = None
    user = request.state.user
    body = await request.body()

    if error:
        if request.state.inspect:
            frame = request.state.inspect
            error_file = frame.f_code.c_filename
            error_func = frame.f_code.co_name
            error_line = frame.f_lineno
        else:
            error_func = error_file = error_line = "UNKNOWN"

        error_log = dict(
            errorFunc=error_func,
            location=f"{str(error_line)} line in {error_file}",
            raised=str(error.__class__.__name__),
            msg=str(error.ex),
        )

    email = user.email.split("@") if user and user.email else None
    user_log = dict(
        client=request.state.ip,
        user=user.id if user and user.id else None,
        email="**" + email[0][2:-1] + "*@" + email[1] if user and user.email else None,
    )

    log_dict = dict(
        url=request.url.hostname + request.url.path,
        method=str(request.method),
        statusCode=status_code,
        errorDetail=error_log,
        client=user_log,
        processedTime=str(round(t * 1000, 5)) + "ms",
        datetimeUTC=datetime.utcnow().strftime(time_format),
        datetimeKR=(datetime.utcnow() + timedelta(hours=9)).strftime(time_format),
    )

    if body:
        log_dict["body"] = body
    if error and error.status_code >= 500:
        logger.error(json.dumps(log_dict))
    else:
        logger.info(json.dumps(log_dict))
