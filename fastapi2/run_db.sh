#/bin/bash
TAG=latest
docker run --rm -d \
        -p 5432:5432 \
        -e POSTGRES_PASSWORD=1234 \
        -e TZ=Asia/Seoul \
        postgres:${TAG}
