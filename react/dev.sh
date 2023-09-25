#/bin/bash

docker build -t my-react .
docker run --rm -d --volume .:/app my-react