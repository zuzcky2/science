#프로그램 개요
이 프로그램은 Python을 사용하여 Docker를 관리하는 데 사용되는 다양한 설정 파일과 스크립트를 포함합니다. 이 프로그램에는 Docker 컨테이너를 설정하고 실행하는 데 필요한 모든 것이 포함되어 있습니다. 주요 구성 요소로는 Dockerfile, docker-compose.yml 및 Bash 스크립트가 있습니다.

하단의 로컬 네트워크 및 호스트 변조부분은 구성에 맞춰 수정할 수 있습니다.

##구성 요소
* Dockerfile: Docker 이미지를 빌드하는 데 사용됩니다. 각 서비스에 대한 Docker 이미지를 만들기 위한 명령 및 환경 설정이 포함되어 있습니다.
* docker-compose.yml: 여러 Docker 서비스를 정의하고 관리하는 데 사용됩니다. 각 서비스의 설정, 환경 변수 및 종속성을 정의합니다.
* Bash 스크립트: Docker 네트워크를 생성하고 관리하는 데 사용됩니다. Docker 컨테이너 및 네트워크를 관리하기 위해 필요한 명령이 포함되어 있습니다.

##구현된 서비스
1. nginx: 웹 서버로 사용되며, 프로젝트의 여러 서비스 및 애플리케이션에 대한 역할을 수행합니다.
2. anaconda: 데이터 과학 및 머신러닝 작업을 위한 Anaconda 환경을 제공합니다. Jupyter Notebook을 실행하고 관리합니다.
3. fastapi: FastAPI를 사용하여 API 서버를 제공합니다.
4. nodejs: Node.js 환경을 제공하며, 프론트엔드(Vue) 애플리케이션을 실행할 수 있습니다.
5. mongodb: MongoDB 데이터베이스를 호스팅하고 관리합니다.
6. logrotate: 로그 파일을 자동으로 로테이트하고 관리합니다.
7. chromium: Selenium Grid를 사용하여 웹 브라우저 테스트 환경을 설정합니다.
8. hub: Selenium Grid의 중앙 집중식 허브를 설정하고 관리합니다.


##사용법
1. 프로그램을 클론합니다:
```bash
git clone https://github.com/zuzcky2/science.git
```
2. 필요한 설정을 수정합니다. 주로 환경 변수를 설정하는 부분입니다.
```bash
cd docker

cp .env.example .env
cp .node.example .node.env
```
3. Docker 네트워크를 생성합니다
```bash
bash ./__docker-network-setup.sh
```
4. Docker 컨테이너를 빌드하고 실행합니다
```bash
bash ./docker-run.sh
```
5. MongoDB 기본 데이터베이스와 유저를 세팅합니다.
```bash
docker-compose exec mongodb sh -c 'bash /var/volumes/docker/user_db_add.sh'
```
6. VueJs 를 빌드합니다.
```bash
bash ./web_build.sh
```

##테스트용 로컬 네트워크 설정
1. 로컬 host 변조
```bash
127.0.0.1      aggrobot.click
127.0.0.1      www.aggrobot.click
127.0.0.1      api.aggrobot.click
127.0.0.1      static.aggrobot.click
127.0.0.1      socket.aggrobot.click
127.0.0.1      jupyter.aggrobot.click
127.0.0.1      vnc.aggrobot.click
127.0.0.1      hub.aggrobot.click
```
2. 필요한 설정을 수정합니다. 주로 환경 변수를 설정하는 부분입니다.
```bash
cd docker/router

cp .env.example .env
```

3. 로컬 라우터를 빌드합니다.
```bash
docker-compose up -d --build
```

4. certbot 을 통해 ssl dns wildcard challenge 를 진행합니다.
```bash
docker-compose exec certbot sh -c 'sh /certbot-certonly.sh'
```

5. haproxy 를 restart 합니다.
```bash
docker-compose exec haproxy restart
```

##주의 사항
각 서비스의 환경 변수와 설정은 사용하는 환경 및 요구 사항에 따라 적절하게 수정해야 합니다.
Docker 및 Docker Compose에 대한 이해가 필요합니다.
스크립트를 실행하기 전에 실행 권한을 부여해야 할 수 있습니다.
