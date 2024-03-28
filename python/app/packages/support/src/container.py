from .abstracts.container import ContainerAbstract, providers
from .modules.env import Env
from .modules.config import Config
from .modules.kst import Kst

class Container(ContainerAbstract):
    """
    컨테이너 클래스입니다.

    Attributes:
        env (Env): 환경 변수를 관리하는 Env 객체입니다.
        kst (Kst): 한국 표준시(KST)의 현재 날짜와 시간을 나타내는 Kst 객체입니다.
    """

    env: Env = providers.Singleton(Env)

    config: Config = providers.Singleton(Config, env=env)

    kst: Kst = providers.Singleton(Kst)