from fastapi import FastAPI, Form, File, UploadFile
from typing import Annotated, Union

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    """
    In the OAuth2, password flow requires fields as username, password, which is exactly
    And they are sent as Form, not JSON

    HTML Form data is encoded using media type 'application/x-www-form-urlencoded'
    But when it is included files, it is encoded as multipart/form-data

    Args:
        username (Annotated[str, Form): _description_
        password (Annotated[str, Form): _description_

    Returns:
        _type_: _description_
    """
    return {"username": username}


# To receive uploaded files, we should install python-multipart pip library
# Becuase it is sent as Form
# If we want to be optional, we could use Union None and set default value to None
@app.post("/file/")
async def create_file(file: Annotated[Union[bytes, None], File()] = None):
    """
    We can recevie files as bytes and be stored in memory
    It will work well for small files
    But there are serveral cases in which we might benefit from using 'UploadFile'

    Args:
        file (Annotated[bytes, File): _description_

    Returns:
        _type_: _description_
    """
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
    file: Annotated[
        Union[UploadFile, None], File(description="Upload file as UploadFile Class")
    ] = None
):
    """
    It use spooled file. it will be stored in disk after passing maximum memory limitation
    It will work well for large files like images, vedio, large banaries, etc ... without consuming all the memory
    We can get a metadata from the uploaded file
    It has a file-like async interface. it exposes a 'SpooledTemporaryFile', file-like object, so we can pass directly to other libaries that expect a file-like object

    UploadFile has filename, content_type(MIME type / media type), file(file-like object)
    It aslo has async method like write(size), read(size), seek(offset), close() that we need to use await

    contents = await myfile.read() (contents = myfile.file.read() in def)

    If we call these aysnc functions, FastAPI runs them in a thread pool and awaits

    Args:
        file (UploadFile): _description_

    Returns:
        _type_: _description_
    """
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}


# We can upload multiple files use list
@app.post("/files/")
async def create_files(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


from fastapi.responses import HTMLResponse


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


# We can define File, Form at the same time
@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True)
