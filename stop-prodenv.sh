#!/bin/bash

export COMPOSE_FILE=production.yml

echo
echo "*********************************************"
echo "This script STOPS the production environment!"
echo "*********************************************"
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

echo "Stopping compose environment..."
docker compose down

echo
echo "Environment Stopped!"
echo
