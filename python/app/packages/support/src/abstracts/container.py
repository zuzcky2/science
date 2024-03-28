from dependency_injector import containers, providers

class ContainerAbstract(containers.DeclarativeContainer):
    """
    종속성 주입을 위한 컨테이너 클래스입니다.

    Attributes:
        config (providers.Configuration): 구성 정보를 제공하는 Configuration 객체입니다.
    """
    config: providers.Configuration = providers.Configuration()