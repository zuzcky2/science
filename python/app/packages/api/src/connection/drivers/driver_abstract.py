from abc import abstractmethod
from typing import Optional

class DriverAbstract:
    """
    드라이버 추상 클래스입니다.
    """

    @abstractmethod
    def set_credentials(self, **options):
        """
        자격 증명을 설정하는 추상 메서드입니다.

        Args:
            **options: 설정 옵션을 포함하는 키워드 인수입니다.
        """
        pass
