from dependency_injector.wiring import Provide, inject
from typing import Union
from .src.container import Container
from .src.connection.connection_manager import ConnectionManager

@inject
def main(
    _connection: ConnectionManager = Provide[Container.connection],
) -> Union[ConnectionManager]:
    """
    주어진 컨테이너로부터 ConnectionManager 를 가져와 반환합니다.

    Parameters:
        _connection (ConnectionManager): 컨테이너로부터 가져온 ConnectionManager 객체입니다.

    Returns:
        Union[ConnectionManager]: 가져온 `ConnectionManager` 객체를 반환합니다.
    """
    return _connection

# 의존성 주입을 위한 컨테이너 생성
application = Container()

# 컨테이너의 구성 요소들을 와이어링합니다.
application.wire(modules=[__name__])

# main 함수 호출하여 driver 객체 획득
connection = main()

# 외부로 노출할 변수들을 지정합니다.
__all__ = ['connection']