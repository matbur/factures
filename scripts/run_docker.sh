#!/bin/bash

docker pull matbur/faccont

docker run \
    -p 8000:8000 \
    --rm \
    matbur/faccont \
    python src/manage.py runserver 0.0.0.0:8000
