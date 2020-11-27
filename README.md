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
Run the tests:
```console
$ docker-compose exec api pytest -p no:warnings
```
[Client repository](https://github.com/Chay23/react-app)

![Alt text](docs/schema_viz.png?raw=true)

![Alt text](docs/10kfeetview.jpg?raw=true)
