#!/bin/bash

echo "Starting Dentify-AI"
# git pull
source ./env/Scripts/activate
python -m pip install -r requirements.txt
cd dentify_ai
python manage.py makemigrations
python manage.py migrate
python manage.py runserver