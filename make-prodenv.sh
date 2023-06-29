#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

echo
echo "************************************************"
echo "This script sets up a new production enviroment!"
echo "************************************************"
echo

read -r -p "Are you sure you want to continue? (yes/no) "
if [ "$REPLY" != "yes" ]; then
  exit 0
fi
echo

read -r -p "Are you sure? (type production to continue) "
if [ "$REPLY" != "production" ]; then
  exit 0
fi
echo

export COMPOSE_FILE=production.yml

echo "Checking .env file..."
if [ ! -f .env ]; then
  echo "[ERROR] Missing .env file! Aborting..."
  echo
  exit 1
fi
echo "Done"

echo "Building compose environment..."
docker compose build

echo "Starting compose environment..."
docker compose up -d

echo
echo "Environment Ready!"
echo
