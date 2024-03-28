from app.packages.support.src.abstracts.connection_manager import ConnectionManagerAbstract
from app.packages.support import config
from .drivers.fastapi_driver import FastAPIDriver
from typing import Optional, Union

class ConnectionManager(ConnectionManagerAbstract):
    """
    연결 관리자 클래스입니다.

    Attributes:
        _DRIVER_FASTAPI (str): FastAPI 드라이버의 이름입니다.
        _driver (Union[FastAPIDriver]): 드라이버 객체입니다.
        default_driver (str): 기본 드라이버 이름입니다.
    """

    _DRIVER_FASTAPI: str = 'fastapi'
    _driver: Union[FastAPIDriver]

    default_driver: str = config.get('api.default_driver')

    def get_driver(self, driver_name: Optional[str] = None) -> Union[FastAPIDriver]:
        """
        지정된 드라이버를 반환합니다.

        Args:
            driver_name (Optional[str]): 드라이버의 이름입니다. 기본값은 None 입니다.

        Returns:
            Union[FastAPIDriver]: 지정된 드라이버 객체입니다.
        """
        driver_name = driver_name if driver_name else self.default_driver
        driver = None

        if driver_name:
            if driver_name == self._DRIVER_FASTAPI:
                driver = FastAPIDriver(**{
                    'redoc_url': config.get('api.redoc_url'),
                    'openapi_url': config.get('api.openapi_url'),
                    'title': config.get('api.title'),
                    'description': config.get('api.description'),
                    'version': config.get('api.version'),
                })

        if driver:
            driver.set_credentials(**{
                'allow_origins': config.get('api.security.allow_origins'),
                'allow_credentials': config.get('api.security.allow_credentials'),
                'allow_methods': config.get('api.security.allow_methods'),
                'allow_headers': config.get('api.security.allow_headers')
            })

            return driver

        self._raise_driver_not_found(driver_name)