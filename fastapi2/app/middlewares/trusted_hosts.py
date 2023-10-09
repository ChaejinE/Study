import typing

from starlette.datastructures import URL, Headers
from starlette.responses import PlainTextResponse, RedirectResponse, Response
from starlette.types import ASGIApp, Receive, Scope, Send

ENFORCE_DOMAIN_WILDCARD = "Domain wildcard patterns must be like '*.example.com'."


class TrustedHostMiddleware:
    def __init__(
        self,
        app: ASGIApp,
        allowed_hosts: typing.Sequence[str] = None,
        except_path: typing.Sequence[str] = None,
        www_redirect: bool = True,
    ) -> None:
        if allowed_hosts is None:
            allowed_hosts = ["*"]
        if except_path is None:
            except_path = []
        for pattern in allowed_hosts:
            assert "*" not in pattern[1:], ENFORCE_DOMAIN_WILDCARD
            if pattern.startswith("*") and pattern != "*":
                assert pattern.startswith("*."), ENFORCE_DOMAIN_WILDCARD

        self._app = app
        self._allowed_hosts = list(allowed_hosts)
        self._allow_any = "*" in allowed_hosts
        self._www_redirect = www_redirect
        self._except_path = list(except_path)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if self._allow_any or scope["type"] not in (
            "http",
            "websocket",
        ):
            """
            모두 허용이거나 http, websocket이면 host 검사하지 않고 main app에 반환
            """
            await self._app(scope, receive, send)
            return

        headers = Headers(scope=scope)
        host = headers.get("host", "").split(":")[0]
        is_valid_host = False
        found_www_redirect = False

        for pattern in self._allowed_hosts:
            if (
                host == pattern
                or (pattern.startswith("*") and host.endswith(pattern[1:]))
                or URL(scope=scope).path in self._except_path
            ):
                is_valid_host = True
                break
            elif "www." + host == pattern:
                found_www_redirect = True

        if is_valid_host:
            await self._app(scope, receive, send)
        else:
            if found_www_redirect and self._www_redirect:
                url = URL(scope=scope)
                redirect_url = url.replace(netloc="www." + url.netloc)
                response = RedirectResponse(Url=str(redirect_url))
            else:
                response = PlainTextResponse("Invalid host header", status_code=400)

            await response(scope, receive, send)
