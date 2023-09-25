#/bin/bash

docker build -t my-react .
docker run --rm -d -p 3000:3000 -v .:/app my-react
