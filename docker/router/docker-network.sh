#!/usr/bin/env bash

# Docker 네트워크 확인 및 생성 스크립트
# 스크립트는 'local-network'라는 이름의 Docker 네트워크를 확인하고 없으면 생성합니다.

# Docker 네트워크 목록 조회 및 'local-network' 확인
cnt=$(docker network list | grep local-network | wc -l)

# 'local-network'가 없으면 생성
if [[ $cnt -eq 0 ]]; then
    docker network create \
      --driver=bridge \
      --subnet=172.210.0.0/16 \
      --ip-range=172.210.100.0/24 \
      --gateway=172.210.100.254 \
      loca
