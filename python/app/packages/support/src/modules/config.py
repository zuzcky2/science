import os
import importlib.util
from typing import Any
from functools import lru_cache
from .env import Env

class Config:
    """
    설정 값을 로드하는 클래스입니다.

    Attributes:
        _CONFIG_MODULE_NAME (str): 각 설정 파일에서 사용할 모듈명입니다.
        _relative_path (str): 설정 파일이 위치한 상대 경로입니다.
        _config_path (str): 설정 파일이 위치한 전체 경로입니다.
        env (Env): 환경 변수를 관리하는 Env 객체입니다.
    """

    _CONFIG_MODULE_NAME = 'configs'
    _relative_path: str
    _config_path: str

    def __init__(self, env: Env):
        """
        Config 클래스의 인스턴스를 초기화합니다.

        Args:
            env (Env): 환경 변수를 관리하는 Env 객체입니다.
        """
        self.env = env
        self._relative_path = 'app/configs'
        self._config_path = os.path.join(self.env.get('PROJECT_ROOT', '/var/workspace/python'), self._relative_path)

    @lru_cache(maxsize=None)  # 캐싱 정책 추가
    def get(self, config: str, default: Any = None) -> Any:
        """
        지정된 설정 값을 가져옵니다.

        Args:
            config (str): 가져올 설정 값의 이름입니다.
            default (Any, optional): 설정 값이 없을 경우 반환할 기본 값입니다. 기본값은 None입니다.

        Returns:
            Any: 설정 값입니다. 설정 값이 없을 경우 기본값이 반환됩니다.
        """
        # 설정 값이 포함된 파일의 전체 경로를 생성합니다.
        configs = config.split('.')
        full_module_path = os.path.join(self._config_path, f'{configs[0]}.py')

        # 설정 파일이나 디렉토리가 존재하지 않으면 기본값을 반환합니다.
        if not os.path.exists(self._config_path) or not os.path.exists(full_module_path):
            return default

        try:
            # 설정 파일을 동적으로 로드합니다.
            module = importlib.import_module(f'{self._relative_path.replace("/", ".")}.{configs[0]}')
            # 로드한 모듈에서 설정 값을 가져옵니다.
            item = module.__getattribute__(self._CONFIG_MODULE_NAME)
            # 설정 값이 여러 단계로 구성되어 있으면 각 단계마다 값을 찾습니다.
            if len(configs) > 1:
                for cfg in configs[1:]:
                    item = item[cfg]
            return item
        except Exception:
            # 에러가 발생하면 기본값을 반환합니다.
            return default
