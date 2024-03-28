#!/usr/bin/env bash

certbot certonly -d ${SERVER_NAME} -d *.${SERVER_NAME} \
--manual --preferred-challenges dns --server https://acme-v02.api.letsencrypt.org/directory \
--email ${MAINTAINER}
