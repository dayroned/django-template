#!/bin/bash

export COMPOSE_FILE=local.yml

if ! ps -ef | grep -v grep | grep run-devenv.sh ; then
    echo "Please run ./run-devenv.sh first"
    exit 1
fi

echo "Testing environment..."
docker compose exec django python manage.py test
