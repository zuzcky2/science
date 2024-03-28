#!/usr/bin/env bash

docker-compose exec anaconda bash -c 'poetry install'
docker-compose exec anaconda bash -c 'bash ./update-dependency.sh'

docker-compose exec fastapi bash -c 'poetry install'
docker-compose exec fastapi bash -c 'bash ./update-dependency.sh'

