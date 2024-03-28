#!/usr/bin/support bash

export __CONTAINER_VOLUME_PATH__

poetry export -f requirements.txt > /var/workspace/python/requirements.txt --without-hashes
poetry export -f requirements.txt > ${__CONTAINER_VOLUME_PATH__}/docker/requirements.txt --without-hashes
pip install -r /var/workspace/python/requirements.txt