#!/bin/bash

export COMPOSE_FILE=production.yaml

if [ $# -ne 1 ]; then
  echo "Usage: $0 <backup_file>"
  exit 1
fi

BACKUP_FILE=$1
TEMP_DIR=$(mktemp -d "/tmp/restore_XXXXXX")

echo
echo "************************************************"
echo "This script RESTORES the production environment!"
echo "************************************************"
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

echo "Checking if the production environment is running..."
if ! docker compose ps | grep -q "Up"; then
  echo "[ERROR] The production environment is not running."
  exit 1
fi
echo

echo "Extracting the backup file..."
tar -xzf "$BACKUP_FILE" -C "$TEMP_DIR"
echo

echo "Restoring media files..."
docker cp "$TEMP_DIR/media/." "$(docker compose ps -q django):/app/media"
echo

echo "Copying the database backup file to the Django container..."
DB_BACKUP_FILE=$(ls $TEMP_DIR/db_backup_*.json)
docker cp "$DB_BACKUP_FILE" "$(docker compose ps -q django):/tmp/db_backup.json"
echo

echo "Restoring the database from the JSON file..."
docker compose exec -T django python manage.py flush --no-input
docker compose exec -T django python manage.py loaddata /tmp/db_backup.json --exclude=contenttypes
echo

echo "Cleaning up..."
rm -rf "$TEMP_DIR"
docker compose exec -T django rm /tmp/db_backup.json
echo

echo "Restore Completed!"
echo
