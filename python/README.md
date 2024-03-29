#구성
이 프로젝트는 다음과 같은 구성 요소로 구성됩니다.

## 1. 패키지
프로젝트에는 여러 패키지가 포함되어 있습니다.

* app.packages.support: 환경 변수 및 시간 관리를 담당하는 패키지
* app.packages.database: 데이터베이스 연결 및 모델을 관리하는 패키지
* app.packages.api: API 연결 및 라우팅을 관리하는 패키지
## 2. 모듈
프로젝트에는 다양한 모듈이 있습니다. 각 모듈은 특정 기능을 수행합니다.

* model.mongodb_model: MongoDB 데이터 모델을 정의하는 모듈
* drivers.fastapi_driver: FastAPI 드라이버를 정의하는 모듈
* support.abstracts.connection_manager: 연결 관리자 추상 클래스를 정의하는 모듈
## 3. 설정
프로젝트 설정은 config 모듈을 통해 관리됩니다. 이 모듈에는 환경 변수 및 기타 설정이 포함되어 있습니다.

## 사용법
이 프로젝트는 다음과 같은 방식으로 사용할 수 있습니다.

* 데이터베이스 연결 설정하기: app.packages.database 패키지를 사용하여 데이터베이스에 연결합니다.
* API 라우팅 설정하기: app.packages.api 패키지를 사용하여 API 엔드포인트를 설정합니다.
* 환경 변수 및 시간 관리하기: app.packages.support 패키지를 사용하여 환경 변수를 관리하고, 시간을 조작합니다.

## 문서
각 패키지의 상세 문서는 아래 정보를 참조하세요.

* [support](./app/packages/support/README.md)
* [database](./app/packages/database/README.md)
* [api](./app/packages/api/README.md)
