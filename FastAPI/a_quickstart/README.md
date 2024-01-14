# Reference
- https://fastapi.tiangolo.com/ko/

# on Local
## using personal python virtual environment
### Setup
```bash
pipenv install --deploy
```

### Run
```bash
uvicorn main:app --reload
```
- main : main.py file name
- app : created object in main.py ```app = FastAPI()```
- --reload : When raised modification code, restart app. use only when developing

## using Docker [Recommand]
### Run container
```bash
IMG=fastapi
TAG=quickstart
docker build -t ${IMG}:${TAG} .
LOCAL_PORT=8000
CONTAINER_PORT=8000
LOCAL_PATH=.
CONTATINER_PATH=/usr/src/app
docker run --rm -d -p ${LOCAL_PORT}:${CONTAINER_PORT} -v ${LOCAL_PATH}:${CONTATINER_PATH} --name ${TAG} ${IMG}:${TAG} python main.py
```
- You can check whether or not operate container using ```docker ps```. it is operated on demon mode
- You can access app using localhost:${LOCAL_PORT} because it is port foward between ${LOCAL_PORT} and ${CONTAINER_PORT}

### Remove container
```bash
IMG=fastapi
TAG=quickstart
docker stop quickstart
```
- Because of ```--rm```, you can just run ```docker stop```

# API Docs
- Swagger UI
```
http://127.0.0.1:8000/docs
```

```
http://127.0.0.1:8000/redoc
```
