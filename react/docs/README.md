```shell
IMG=app
TAG=test
docker build -t ${IMG}:${TAG} .
TARGET_PROJECT=vite-project
cd ${TARGET_PROJECT}
docker run --rm -d -it -v .:/usr/src -p 5173:5173 ${IMG}:${TAG}
cd -
```
