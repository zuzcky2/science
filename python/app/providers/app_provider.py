from app.packages.support import env, kst, config
from app.packages.database import connection as database_connection
from app.packages.api import connection as api_connection
from fastapi import FastAPI
from app.http.routes.route import router
from app.packages.support.src.abstracts.provider import ProviderAbstract
from app.packages.database.src.connection.drivers.mongodb import MongodbDriver

class AppProvider(ProviderAbstract):
    """
    AppProvider 클래스는 애플리케이션의 제공자 역할을 수행합니다.
    """

    def __init__(self):
        """
        AppProvider 클래스의 생성자입니다.
        """
        self.env = env
        self.kst = kst
        self.config = config
        self.api: FastAPI = api_connection.driver.app
        self.database: MongodbDriver = database_connection.driver

    def boot(self):
        """
        애플리케이션을 부팅합니다.
        """
        self.set_api()

    def set_api(self):
        """
        API 라우터를 설정합니다.
        """
        self.api.include_router(router)


provider = AppProvider()
provider.boot()

__all__ = ['provider']
