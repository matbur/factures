#!/bin/bash

rm -f src/db.sqlite3
find -name 000* | xargs rm -f
python src/manage.py makemigrations
python src/manage.py migrate
python src/manage.py loaddata fixtures/*

