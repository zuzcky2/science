from ...support.src.abstracts.container import ContainerAbstract, providers
from .connection.connection_manager import ConnectionManager

class Container(ContainerAbstract):
    """
    의존성 주입을 사용하여 컨테이너를 초기화하는 클래스입니다.

    Attributes:
        driver (ConnectionManager): api 관리자 객체입니다.
    """

    # api 관리자 객체를 싱글톤으로 제공합니다.
    connection: ConnectionManager = providers.Singleton(ConnectionManager)
