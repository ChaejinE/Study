# Refernec
- https://fastapi.tiangolo.com/tutorial/path-params/
- https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
- https://fastapi.tiangolo.com/tutorial/path-operation-configuration/

# Docker Run
```bash
IMG=fastapi
TAG=pathparamter
docker build -t ${IMG}:${TAG} .
LOCAL_PORT=8003
CONTAINER_PORT=8000
LOCAL_PATH=.
CONTATINER_PATH=/usr/src/app
docker run --rm -d -p ${LOCAL_PORT}:${CONTAINER_PORT} -v ${LOCAL_PATH}:${CONTATINER_PATH} --name ${TAG} ${IMG}:${TAG} python main.py
```

# Docker Stop
```bash
TAG=pathparamter
docker stop ${TAG}
```

# Docker Delete Image for you disk
```bash
IMG=fastapi
TAG=queryparameter
docker rmi ${IMG}:${TAG}
```
