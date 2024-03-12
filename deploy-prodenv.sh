#!/bin/bash

export COMPOSE_FILE=production.yaml

INGRESS_WEB=ingress-web

echo
echo "**********************************************"
echo "This script STARTS the production environment!"
echo "**********************************************"
echo

if [ -z "${AUTO_DEPLOY:-}" ]; then
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
fi

echo "Checking .env file..."
if [ ! -f .env ]; then
  echo "[ERROR] Missing .env file! Aborting..."
  exit 1
fi
echo

echo "Creating ${INGRESS_WEB} network if it doesn't exists..."
if [ ! "$(docker network ls -q -f name=${INGRESS_WEB})" ]; then
  docker network create ${INGRESS_WEB}
fi
echo

echo "Stopping compose environment if it is running..."
docker compose down
echo

echo "Building compose environment..."
docker compose build
echo

echo "Starting compose environment..."
docker compose up -d
echo

echo "Environment Ready!"
echo
