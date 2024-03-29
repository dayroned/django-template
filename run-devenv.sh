#!/bin/bash

export COMPOSE_FILE=local.yml

stop_stack()
{
    echo "Stopping compose environment..."
    docker compose down

    echo "Removing media directory..."
    if [ -d media ]; then
        rm -rf media
    fi
}

if [ ! -f .env ]; then
    echo "Creating .env file from example..."
    cp .env.example .env
fi

echo "Creating media directory..."
mkdir -p media

echo "Building compose environment..."
docker compose build

echo "Starting compose environment..."
docker compose up -d

trap stop_stack INT

echo
echo "System running at http://localhost:8000"
echo

echo "Django logs..."
docker compose logs django -f
