# Proyecto de ejemplo usando TDD - Python y Django

[![Build Status](https://travis-ci.org/josemlp91/tdd-with-python.svg?branch=master)](https://travis-ci.org/josemlp91/tdd-with-python)

Proyecto de aprendizaje de la filosofia TDD, unido a Docker y el editor Visual Studio.

## Instalación

    docker build -t tddwithpython .

## Ejecutar servidor.

    docker-compose up

## Ejecutar test

    docker-compose run web python ./superlists/manage.py test lists


## Travis CI

![](https://i.imgur.com/5JpivPd.png)


## Heroku 

Para intalar Heroku CLI usar:
    curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
