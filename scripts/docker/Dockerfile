FROM ubuntu:16.10
RUN apt-get update
RUN apt-get install -y python3.6 python3-pip git
RUN git clone https://github.com/matbur95/factures.git
WORKDIR factures
RUN ln /usr/bin/python3.6 /usr/bin/python
RUN alias python='python3.6'
RUN python -m pip install -r requirements.txt
RUN python src/manage.py makemigrations
RUN python src/manage.py migrate
RUN python src/manage.py loaddata fixtures/*
