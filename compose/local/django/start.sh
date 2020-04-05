#!/bin/sh

python manage.py migrate
python manage.py loaddata config/fixtures/*.json

python manage.py runserver 0.0.0.0:8000
