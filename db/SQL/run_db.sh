#!/bin/bash

export POSTGRES_PASSWORD=1234
export POSTGRES_USER="basic"
export POSTGRES_DB="practice"

docker run --rm \
           -d \
           -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
           -e POSTGRES_USER=${POSTGRES_USER} \
           -e POSTGRES_DB=${POSTGRES_DB} \
           postgres:latest