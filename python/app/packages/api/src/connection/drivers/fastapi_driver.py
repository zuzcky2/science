from fastapi import FastAPI
from .driver_abstract import DriverAbstract
from starlette.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi


class FastAPIDriver(DriverAbstract):
    """
    FastAPI 드라이버 클래스입니다.
    """

    def __init__(self, **options):
        self.app = FastAPI(
            redoc_url=options.get('redoc_url', None),
            openapi_url=options.get('openapi_url', None),
            title=options.get('title', None),
            description=options.get('description', None),
            version=options.get('version', None),
        )

    def set_credentials(self, **options):
        """
        CORS 미들웨어를 추가하여 인증 정보를 설정합니다.

        Args:
            **options: 설정할 인증 옵션을 포함하는 키워드 인수입니다.
                - allow_origins (Optional[List[str]]): 허용된 오리진(origin) 목록입니다. 기본값은 빈 리스트입니다.
                - allow_credentials (bool): 자격 증명(credential) 허용 여부입니다. 기본값은 False 입니다.
                - allow_methods (Optional[List[str]]): 허용된 HTTP 메서드 목록입니다. 기본값은 빈 리스트입니다.
                - allow_headers (Optional[List[str]]): 허용된 HTTP 헤더 목록입니다. 기본값은 빈 리스트입니다.
        """
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=options.get('allow_origins', []),
            allow_credentials=options.get('allow_credentials', False),
            allow_methods=options.get('allow_methods', []),
            allow_headers=options.get('allow_headers', [])
        )
