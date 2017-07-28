#!/usr/bin/env sh

set -e

python manage.py makemigrations
python manage.py migrate
gunicorn cutetube.wsgi -b :8000

exec "$@"

