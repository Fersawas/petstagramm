#!/bin/bash

set -e

python manage.py wait_for_db
python manage.py migrate --no-input
python manage.py collectstatic --no-input
cp -r /app/collected_static/. /backend_static/static/

gunicorn petstagramm.wsgi:application --bind 0.0.0.0:8000 --reload