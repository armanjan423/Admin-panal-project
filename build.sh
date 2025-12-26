#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
# python manage.py migrate # Not needed for mongoengine usually, but keep if using Django DBs
