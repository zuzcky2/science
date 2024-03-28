from typing import Optional, Union
from app.packages.database.src.connection.drivers.mongodb import MongodbDriver
from app.packages.support import config
from app.packages.support.src.abstracts.connection_manager import ConnectionManagerAbstract


class ConnectionManager(ConnectionManagerAbstract):
    """
    드라이버 관리 클래스입니다. MongoDB와 같은 여러 데이터베이스 드라이버를 관리합니다.
    """
    _DRIVER_MONGODB: str = 'mongodb'

    default_driver: str = config.get('database.default_driver')
    _driver: Union[MongodbDriver]

    def get_driver(self, driver_name: Optional[str] = None) -> Union[MongodbDriver]:
        """
        지정된 이름의 드라이버를 가져옵니다.

        Args:
            driver_name (Optional[str]): 가져올 드라이버의 이름입니다.

        Returns:
            Union[MongodbDriver]: 드라이버를 반환합니다.

        Raises:
            ValueError: 드라이버를 찾을 수 없는 경우 예외가 발생합니다.
        """
        driver_name = driver_name if driver_name else self.default_driver
        conn = config.get(f'database.{driver_name}')

        if driver_name and conn:
            if driver_name == self._DRIVER_MONGODB:
                return MongodbDriver().set_connection(conn)

        self._raise_driver_not_found(driver_name)

