#!/bin/bash

python ./superlists/manage.py migrate

python ./superlists/manage.py runserver 0.0.0.0:80