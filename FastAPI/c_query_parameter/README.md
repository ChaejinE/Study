# Reference
- https://fastapi.tiangolo.com/tutorial/query-params/
- https://fastapi.tiangolo.com/tutorial/query-params-str-validations/

# Docker Run
```bash
IMG=fastapi
TAG=queryparameter
docker build -t ${IMG}:${TAG} .
LOCAL_PORT=8003
CONTAINER_PORT=8000
LOCAL_PATH=.
CONTATINER_PATH=/usr/src/app
docker run --rm -d -p ${LOCAL_PORT}:${CONTAINER_PORT} -v ${LOCAL_PATH}:${CONTATINER_PATH} --name ${TAG} ${IMG}:${TAG} python main.py
```

# Docker Stop
```bash
TAG=queryparameter
docker stop ${TAG}
```

# Docker Delete Image for you disk
```bash
IMG=fastapi
TAG=queryparameter
docker rmi ${IMG}:${TAG}
```
