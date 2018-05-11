# Proyecto de ejemplo usando TDD - Python y Django

Proyecto de aprendizaje de la filosofia TDD, unido a Docker y el editor Visual Studio.

## Instalación

    docker build -t tddwithpython .

## Ejecutar servidor.

    docker-compose up

## Ejecutar test

    docker-compose run web python ./superlists/manage.py test lists
