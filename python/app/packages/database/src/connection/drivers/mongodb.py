import pymongo
import urllib.parse
from typing import Optional
from .driver_abstract import DriverAbstract

class MongodbDriver(DriverAbstract):
    """
    MongoDB 연결 관리 클래스입니다.
    """

    default_database: str

    def set_connection(self, conn: dict) -> 'MongodbDriver':
        """
        MongoDB에 연결합니다.

        Args:
            conn (dict): MongoDB 연결 설정이 포함된 사전

        Returns:
            MongodbDriver: 자체 객체
        """
        self.default_database = conn['name']

        self._connection = pymongo.MongoClient(
            f"mongodb://{conn['user']}:{urllib.parse.quote(conn['pass'])}"
            f"@{conn['host']}:{conn['port']}/{conn['name']}"
        )

        return self

    def get_connection(self) -> pymongo.MongoClient:
        """
        MongoDB 연결을 반환합니다.

        Returns:
            pymongo.MongoClient: MongoDB 연결 객체

        Raises:
            ValueError: MongoDB 연결이 준비되지 않은 경우
        """
        if not self._connection:
            self._raise_not_prepare_connection()
        return self._connection

    def get_database(self, database_name: str) -> pymongo.mongo_client.database.Database:
        """
        MongoDB 데이터베이스를 반환합니다.

        Args:
            database_name (str): 반환할 데이터베이스의 이름

        Returns:
            pymongo.mongo_client.database: MongoDB 데이터베이스 객체

        Raises:
            ValueError: MongoDB 연결이 준비되지 않은 경우
        """
        if not self._connection:
            self._raise_not_prepare_connection()
        return self._connection.get_database(database_name)