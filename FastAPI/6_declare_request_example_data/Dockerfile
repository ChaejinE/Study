FROM python:3.9-slim

RUN apt-get update && apt-get install -y build-essential git
RUN pip install --upgrade pip && pip install pipenv

ARG WORK_DIR=/usr/src/app
WORKDIR ${WORK_DIR}
COPY Pipfile* .
RUN pipenv install --deploy --system && rm -rf Pipfile*
