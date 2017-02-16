#!/bin/bash

rm -f db.sqlite3
find -name 000* | xargs rm -f
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/*
python manage.py runserver

