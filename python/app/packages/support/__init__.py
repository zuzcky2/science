from dependency_injector.wiring import Provide, inject
from .src.container import Container
from .src.modules.env import Env
from .src.modules.config import Config
from .src.modules.kst import Kst

@inject
def main(
    env_module: Env = Provide[Container.env],
    config_module: Config = Provide[Container.config],
    kst_module: Kst = Provide[Container.kst],
) -> tuple:
    """
    주어진 환경 변수 및 KST 객체를 가져와 튜플로 반환합니다.

    Parameters:
        env_module (Env): 환경 변수를 관리하는 Env 객체입니다.
        config_module (Env): config 변수를 관리하는 Config 객체입니다.
        kst_module (Kst): 한국 표준시(KST)의 현재 날짜와 시간을 나타내는 Kst 객체입니다.

    Returns:
        tuple: 환경 변수 객체와 KST 객체로 이루어진 튜플입니다.
        :param kst_module:
        :param config_module:
        :param env_module:
    """
    return env_module, config_module, kst_module

# Container 인스턴스 생성
application = Container()

# 의존성 주입 설정
application.wire(modules=[__name__])

# main 함수 호출하여 env 와 config 와 kst 객체 생성
env, config, kst= main()

# 외부에서 접근 가능한 객체 목록 지정
__all__ = ['env', 'config', 'kst']