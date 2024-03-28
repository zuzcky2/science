from abc import ABC, abstractmethod
from typing import Any

class DriverAbstract(ABC):
    """
    추상 드라이버 클래스입니다.
    """
    _connection: Any

    @abstractmethod
    def set_connection(self):
        """
        연결 설정을 수행합니다.
        """
        pass

    @abstractmethod
    def get_connection(self):
        """
        연결을 반환합니다.

        Returns:
            연결 객체
        """
        pass

    @abstractmethod
    def get_database(self, database_name: str):
        """
        데이터베이스를 반환합니다.

        Args:
            database_name (str): 반환할 데이터베이스의 이름

        Returns:
            데이터베이스 객체
        """
        pass

    def _raise_not_prepare_connection(self, driver: str = ''):
        """
        연결이 준비되지 않았을 때 ValueError 를 발생시킵니다.
        """
        raise ValueError(f'{driver} 연결이 준비되지 않았습니다.')

    def _raise_not_available_driver(self, driver: str = ''):
        """
        드라이버가 없거나, 허용 가능한 드라이버가 아닐 때 ValueError 를 발생시킵니다.
        """
        raise ValueError(f'드라이버가 없거나, 허용 가능한 드라이버가 아닙니다. {driver}')
