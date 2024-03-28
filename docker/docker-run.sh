#!/usr/bin/env bash

# @author jinsoo.kim <jjambbongjoa@gmail.com>
MSG_COLOR="\033[1;32m"
MSG_RESET="\033[0m"
MSG_PREFIX="${MSG_COLOR}[Jinsoo.Kim@IAPI-WORK-STATUS]$ ${MSG_RESET}"

echo -e "${MSG_PREFIX}서비스 빌드 가능성 검사 시작..\n"
if [ ! -f .env ]; then
    echo "${MSG_PREFIX}#ERROR .env 파일이 존재하지않습니다."
    exit
fi
if [ ! -f docker-compose.yml ]; then
    echo "${MSG_PREFIX}#ERROR docker-compose.yml 파일이 존재하지않습니다."
    exit
fi

echo -e "${MSG_PREFIX}서비스 빌드 가능성 검사 통과\n"

source .env

#echo -e "${MSG_PREFIX}docker network 세팅 시작...\n"
#bash ./__docker-network-setup.sh
#echo -e "${MSG_PREFIX}docker network 세팅 완료\n"


echo -e "${MSG_PREFIX}log, data 디렉토리 세팅 시작...\n"

DIRECTORY="${__VOLUME_PATH__}/dist"
if [ ! -d "$DIRECTORY" ]; then
    mkdir -p ${DIRECTORY}
    chmod 707 ${DIRECTORY}
fi

DIRECTORY="${__VOLUME_PATH__}/log/nginx"
if [ ! -d "$DIRECTORY" ]; then
    mkdir -p ${DIRECTORY}
    chmod 707 ${DIRECTORY}
fi

DIRECTORY="${__VOLUME_PATH__}/log/anaconda"
if [ ! -d "$DIRECTORY" ]; then
    mkdir -p ${DIRECTORY}
    chmod 707 ${DIRECTORY}
fi

DIRECTORY="${__VOLUME_PATH__}/log/fastapi"
if [ ! -d "$DIRECTORY" ]; then
    mkdir -p ${DIRECTORY}
    chmod 707 ${DIRECTORY}
fi

DIRECTORY="${__VOLUME_PATH__}/log/mongodb"
if [ ! -d "$DIRECTORY" ]; then
    mkdir -p ${DIRECTORY}
      chmod 777 ${DIRECTORY}
fi

DIRECTORY="${__VOLUME_PATH__}/data/mongodb"
if [ ! -d "$DIRECTORY" ]; then
    mkdir -p ${DIRECTORY}/db
    chmod 707 ${DIRECTORY}/db
fi

echo -e "${MSG_PREFIX}log, data 디렉토리 세팅 완료\n"

echo -e "${MSG_PREFIX}environment 결합작업 시작...\n"

export MONGO_INITDB_ROOT_USERNAME
export MONGO_INITDB_ROOT_PASSWORD
export MONGO_INITDB_DATABASE
export MONGO_INITDB_USERNAME
export MONGO_INITDB_PASSWORD
export MONGO_INITDB_HOST
export MONGO_INITDB_PORT

export SERVER_NAME
export WEB_SERVER_NAME
export API_SERVER_NAME
export STATIC_SERVER_NAME
export SOCKET_SERVER_NAME
export JUPYTER_SERVER_NAME
export VNC_SERVER_NAME
export HUB_SERVER_NAME
export SYNC_SERVER_NAME
export WEB_URL
export API_URL
export STATIC_URL
export SOCKET_URL
export JUPYTER_URL
export __OPEN_WEB_PORT__
export NODEJS_ENV
export SSL_FILE_NAME

export __CONTAINER_VOLUME_PATH__

envsubst '${SERVER_NAME} ${WEB_SERVER_NAME} ${API_SERVER_NAME} ${STATIC_SERVER_NAME} \
${SOCKET_SERVER_NAME} \
${WEB_URL} ${API_URL} ${STATIC_URL} ${SOCKET_URL} \
${__OPEN_WEB_PORT__} ${NODEJS_ENV}' < ./.node.example > ./.node.env

envsubst '${SERVER_NAME} ${WEB_SERVER_NAME} ${API_SERVER_NAME} ${STATIC_SERVER_NAME} \
${SOCKET_SERVER_NAME} ${JUPYTER_SERVER_NAME} ${VNC_SERVER_NAME} ${HUB_SERVER_NAME} ${SYNC_SERVER_NAME} \
${__CONTAINER_VOLUME_PATH__} ${SSL_FILE_NAME}' < nginx/sites-available/http.conf > nginx/sites-enabled/http.conf

envsubst '${MONGO_INITDB_ROOT_USERNAME} ${MONGO_INITDB_ROOT_PASSWORD} ${MONGO_INITDB_DATABASE} \
${MONGO_INITDB_USERNAME} ${MONGO_INITDB_PASSWORD}' < mongodb/user_db_add_default.sh > mongodb/user_db_add.sh

echo -e "${MSG_PREFIX}environment 결합작업 완료\n"

echo -e "${MSG_PREFIX}서비스 인스턴스 빌드 시작...\n"

docker-compose up --build -d

echo -e "${MSG_PREFIX}서비스 인스턴스 빌드 완료\n"

docker-compose cp ./.node.env nodejs:${__CONTAINER_SOURCE_PATH__}/nodejs/.env

