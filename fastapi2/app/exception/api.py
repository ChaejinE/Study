from starlette import status


class APIException(Exception):
    status_code: int
    code: str
    msg: str
    detail: str
    ex: Exception

    def __init__(
        self,
        *,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        code: str = "0000000",
        msg: str = None,
        detail: str = None,
        ex: Exception = None,
    ) -> None:
        self.status_code = status_code
        self.code = code
        self.msg = msg
        self.detail = detail
        self.ex = ex
        super().__init__(ex)


class NotFoundUserEx(APIException):
    def __init__(self, user_id: int = None, ex: Exception = None) -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            code=f"{status.HTTP_400_BAD_REQUEST}{'1'.zfill(4)}",
            msg="해당유저를 찾을 수 없습니다.",
            detail=f"Not Found User ID : {user_id}",
            ex=ex,
        )


class NotAuthorized(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            code=f"{status.HTTP_401_UNAUTHORIZED}{'1'.zfill(4)}",
            msg="로그인이 필요한 서비스입니다.",
            detail=f"Authorization Required",
            ex=ex,
        )


class TokenExpiredEx(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            code=f"{status.HTTP_400_BAD_REQUEST}{'1'.zfill(4)}",
            msg="세션이 만료되어 로그아웃 되었습니다.",
            detail=f"Token Expired",
            ex=ex,
        )


class TokenDecodeEx(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            code=f"{status.HTTP_400_BAD_REQUEST}{'2'.zfill(4)}",
            msg="비정상적인 접근입니다.",
            detail=f"Token has been compromised",
            ex=ex,
        )
