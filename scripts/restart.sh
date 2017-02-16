#!/bin/bash

rm db.sqlite3
find -name 000* | xargs rm
#python manage.py makemigrations
#python manage.py migrate
#python manage.py loaddata scripts/superuser.json
#python manage.py runserver

