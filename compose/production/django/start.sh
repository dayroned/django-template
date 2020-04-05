#!/bin/sh

python manage.py migrate --settings=config.settings.prod
python manage.py collectstatic --noinput --settings=config.settings.prod

gunicorn config.wsgi --bind 0.0.0.0:5000 --chdir=/app
