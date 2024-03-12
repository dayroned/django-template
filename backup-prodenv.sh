#!/bin/bash

export COMPOSE_FILE=production.yml

BACKUP_DIR="data"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
FILENAME="backup_$DATE.tar.gz"

TEMP_DIR=$(mktemp -d "/tmp/backup_$DATE.XXXXXX")

echo
echo "***********************************************"
echo "This script BACKUPS the production environment!"
echo "***********************************************"
echo

if [ -z "${AUTO_DEPLOY:-}" ]; then
  read -r -p "Are you sure you want to continue? (yes/no) "
  if [ "$REPLY" != "yes" ]; then
    exit 0
  fi
  echo
fi

echo "Checking if the production environment is running..."
if ! docker compose ps | grep -q "Up"; then
  echo "The production environment is not running."
  exit 1
fi
echo "Done"
echo

echo "Exporting the database to a JSON file..."
docker compose exec -T django python manage.py dumpdata --exclude=contenttypes --indent 2 > "$TEMP_DIR/db_backup_$DATE.json"
echo "Done"
echo

echo "Copying media files..."
mkdir -p "$TEMP_DIR/media"
docker cp -q "$(docker compose ps -q django):/app/media/." "$TEMP_DIR/media"
echo "Done"
echo

echo "Creating the backup file..."
mkdir -p "$BACKUP_DIR"
cd "$BACKUP_DIR" || exit
tar -czf "$FILENAME" -C "$TEMP_DIR" .
echo "Done"
echo

echo "Cleaning up..."
rm -rf "$TEMP_DIR"
echo "Done"
echo

echo "Backup created: $FILENAME"
echo
