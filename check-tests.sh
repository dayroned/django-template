#!/bin/bash

export COMPOSE_FILE=local.yaml

if ! ps -ef | grep -v grep | grep run-devenv.sh ; then
    echo "[ERROR] Run ./run-devenv.sh before checking tests."
    exit 1
fi

echo "Testing environment..."
docker compose exec django python manage.py test
