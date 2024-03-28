from abc import abstractmethod
from typing import Union, Optional

class ConnectionManagerAbstract:
    """
    드라이버 관리 클래스입니다.

    Methods:
        __init__(): 클래스 인스턴스를 초기화합니다.
        get_driver(driver_name: Optional[str] = None) -> Union: 지정된 이름의 드라이버를 가져옵니다.
        _raise_driver_not_found(driver_name: str): 드라이버를 찾을 수 없을 때 예외를 발생시킵니다.
    """
    _DRIVER_NOT_FOUND_MSG = '{} driver 가 존재하지 않습니다.'

    default_driver: str
    _driver: Union

    def __init__(self):
        """
        클래스 인스턴스를 초기화합니다.
        """
        self._driver = self.get_driver(self.default_driver)

    @property
    def driver(self) -> Union:
        """
        기본 드라이버를 가져옵니다.
        """
        return self._driver

    @abstractmethod
    def get_driver(self, driver_name: Optional[str] = None) -> Union:
        pass

    @staticmethod
    def _raise_driver_not_found(driver_name: str):
        """
        드라이버를 찾을 수 없을 때 예외를 발생시킵니다.

        Args:
            driver_name (str): 찾을 수 없는 드라이버의 이름입니다.

        Raises:
            ValueError: 드라이버를 찾을 수 없는 경우 예외가 발생합니다.
        """
        raise ValueError(ConnectionManagerAbstract._DRIVER_NOT_FOUND_MSG.format(driver_name))