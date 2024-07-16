#!/bin/bash

export COMPOSE_FILE=local.yaml

stop_stack()
{
    echo "Stopping compose environment..."
    docker compose down
}

echo "Creating .env file from example..."
cp .env.example .env
echo

echo "Creating media directory..."
mkdir -p media
echo

echo "Building compose environment..."
docker compose build
echo

echo "Starting compose environment..."
docker compose up -d
echo

trap stop_stack INT

echo "Environment logs..."
docker compose logs django -f
