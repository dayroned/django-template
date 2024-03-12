#!/bin/sh

echo "Waiting for PostgreSQL to become available..."
while ! nc -z "$SQL_HOST" 5432; do
  sleep 0.1
done
echo "PostgreSQL is available"
echo

echo "Running migrations and loading fixtures..."
python manage.py migrate
python manage.py loaddata config/fixtures/*.json
echo

echo "Starting Django development server..."
python manage.py runserver 0.0.0.0:8000
