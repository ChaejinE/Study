# Reference
- https://fastapi.tiangolo.com/tutorial/extra-models/

# Docker Run
```bash
IMG=fastapi
TAG=extramodels
docker build -t ${IMG}:${TAG} .
LOCAL_PORT=8003
CONTAINER_PORT=8000
LOCAL_PATH=.
CONTATINER_PATH=/usr/src/app
docker run --rm -d -p ${LOCAL_PORT}:${CONTAINER_PORT} -v ${LOCAL_PATH}:${CONTATINER_PATH} --name ${TAG} ${IMG}:${TAG} python main.py
```

# Docker Stop
```bash
TAG=extramodels
docker stop ${TAG}
```

# Docker Delete Image for you disk
```bash
IMG=fastapi
TAG=extramodels
docker rmi ${IMG}:${TAG}
```
