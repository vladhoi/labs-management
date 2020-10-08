Labs management

[![pipeline status](https://gitlab.com/vladhoi/labs-management/badges/main/pipeline.svg)](https://gitlab.com/vladhoi/labs-management/commits/main)


Build the images:
```console
$ docker-compose build
```
Run the containers:
```console
$ docker-compose up -d
```
Create migrations:
```console
$ docker-compose exec api python manage.py makemigrations
```
Apply migrations:
```console
$ docker-compose exec api python manage.py migrate
```
Run the tests:
```console
$ docker-compose exec api pytest -p no:warnings
```
Lint:
```console
$ docker-compose exec api flake8 .
```
Run Black:
```console
$ docker-compose exec api black --exclude="migrations|env" . 
```
Db:
```console
$ docker-compose exec <service-name> psql -d movies_dev -U movies
```