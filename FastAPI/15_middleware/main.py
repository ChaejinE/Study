import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # after process call_next, response is added to X-Process-Time header and returned
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

"""
Origin : Comibation of protocol, domain and port
    http://localhost
    https://localhost
    http://localhost:8080
they are different origin each other
"""

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

from fastapi.middleware.cors import CORSMiddleware

# allow_origins : A list of origins that should be permitted to make cross-origin reuqests
# allow_origin_regex : A regex string to match like https://.*\.example\.org
# allow_methods : A list of HTTP methods. default ['GET']
# allow_headers : A list of HTTP reuqest headers. default [] The Accept, Accept-Language, Content-Language and Content-Type are always allowed
# allow_credentials : Indicate that cookies should be supported for cross-origin requests
# expose_headers : Indicate any response headers that should be made accessible to the browser
# max_age : Maximum time in seconds for browser to chace CORS responses
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
