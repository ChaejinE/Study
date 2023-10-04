#/bin/bash
APP_NAME=fastapi-study
docker build -f Dockerfile.dev -t ${APP_NAME}:latest .
docker run --rm -p 8000:8000 -v ./app:/usr/src/app ${APP_NAME}
