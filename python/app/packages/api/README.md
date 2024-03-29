# API 패키지
이 패키지는 API 라우터, document 기능을 제공하는 유틸리티 모음입니다. FastAPI를 기본으로 지원하며, Pydantic을 사용하여 데이터 모델링을 수행합니다.

### 기능
* 연결 관리: 패키지는 API 연결 관리를 허용하는 'ConnectionManager' 클래스를 제공합니다. API에 대한 연결 설정, 인증 처리 및 연결 설정 관리를 위한 방법을 제공합니다.
* 경로 처리: 패키지는 'Router' 클래스를 사용하여 API 경로 정의를 활성화하고 들어오는 요청을 적절한 처리기 기능으로 보냅니다. 이를 통해 애플리케이션 내에서 API 엔드포인트를 구성하고 관리할 수 있습니다.

## 사용법
```python
from app.packages.api import connection
from app.packages.api.src.http.fastapi_route import router
from fastapi import FastAPI

@router.get('/')
def root():
    return 'Hello World!'

api: FastAPI
api = connection.driver.app

api.include_router(router)
```

## FastAPI
기본적으로 app/providers/app_provider.py 에서 api driver 를 호출하여 docker 의 fastapi container에서 이를 실행합니다.
사용자 측면에서는 app/http/routes/route.py 를 작성하여 fastapi container에서 사용할 수 있습니다.
