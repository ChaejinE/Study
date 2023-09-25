#/bin/bash

docker build -f Dockerfile.dev -t my-react:latest .
docker run --rm -d -p 3000:3000 -v .:/app my-react
