#/bin/bash
APP_NAME=shop

docker build -f Dockerfile.dev -t ${APP_NAME}:latest .
docker run --rm -d -p 3000:3000 -v .:/app ${APP_NAME}
