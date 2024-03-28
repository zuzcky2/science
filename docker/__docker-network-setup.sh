#!/usr/bin/env bash

# Docker 네트워크가 있는지 확인하고 없으면 생성합니다.
cnt=$(docker network list | grep mlops | wc -l)
if [[ $cnt -eq 0 ]]; then
    docker network create \
      --driver=bridge \
      --subnet=172.213.0.0/16 \
      --ip-range=172.213.100.0/24 \
      --gateway=172.213.100.254 \
      mlops
fi
