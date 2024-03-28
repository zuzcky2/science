import os
from dotenv import dotenv_values
from collections import OrderedDict
from pydantic import Field
from typing import Union, Optional
from distutils.util import strtobool
from typing import Any
import numpy as np

class Env:
    """
    프로젝트의 환경 변수를 관리합니다.

    Attributes:
        items (dotenv_values): .env 파일과 환경 변수에서 불러온 값들을 포함하는 OrderedDict 입니다.
    """
    __items: dotenv_values = OrderedDict({**dict(dotenv_values('{}/.env'.format(os.environ['PROJECT_ROOT']))),
                     **dict(OrderedDict(os.environ))})

    def __init__(self):
        self.__cached_values = {}  # 환경 변수 값을 캐싱하기 위한 딕셔너리

    def get(self, key: Optional[str] = None, default: Any = None) -> Union[str, int, float, None]:
        """
        주어진 키에 해당하는 환경 변수 값을 반환하거나 전체 환경 변수 값을 반환합니다.

        Parameters:
            key (str, optional): 프로젝트 .env 에서 불러올 키 값입니다. 기본값은 None 으로, 전체 환경 변수 값을 반환합니다.
            default (Any): 값이 없을경우 기본값을 지정합니다.

        Returns:
            변환된 값, 전체 환경 변수 값 또는 None.
        """
        try:
            # 캐싱된 값이 있으면 바로 반환합니다.
            if key in self.__cached_values:
                return self.__cached_values[key]

            # 캐싱된 값이 없으면 환경 변수 값을 읽어옵니다.
            value = self.__items.get(key)
            if value is None:
                return default

            # 환경 변수 값 유효성 검사를 추가합니다.
            converted_value = self.convert_value(value)
            if converted_value is None:
                return default

            # 캐시에 값을 저장하고 반환합니다.
            self.__cached_values[key] = converted_value
            return converted_value
        except Exception as e:
            # print(f"'{key}'에 대한 값을 가져오는 도중 오류가 발생했습니다: {e}")
            return default

    def convert_value(self,
                        value: str = Field(title='값', description='.env 특정 키에 정의된 값')
                        ) -> Union[str, int, float, None]:
        """
        주어진 문자열 값을 변환합니다.

        Parameters:
            value (str): 변환할 값. 기본값은 '.env 특정 키에 정의된 값'입니다.

        Returns:
            변환된 값 또는 None.

        변환 규칙:
            - 문자열이 'true' 또는 'false' 인 경우에는 bool 값으로 변환합니다.
            - 숫자인 경우에는 정수 또는 소수로 변환합니다.

        예외 처리:
            - 변환할 수 없는 값이 주어진 경우에는 None 을 반환합니다.
            - 최종적으로 검사할 조건이 없으면 주어진 값을 그대로 반환합니다.
        """
        try:
            # 문자열이 'true' 또는 'false' 인 경우에는 bool 값으로 변환합니다.
            if value.lower() in ['true', 'false']:
                return bool(strtobool(value))
            else:
                # 숫자인 경우 정수 또는 소수로 변환합니다.
                num_value = np.float64(value)
                if num_value.is_integer():  # 만약 숫자가 정수인 경우
                    return int(num_value)  # 정수로 변환하여 반환합니다.
                else:
                    return num_value  # 소수인 경우 그대로 반환합니다.
        except ValueError as e:
            # 변환할 수 없는 값이 주어진 경우 에러 메시지를 출력하고 None 을 반환합니다.
            # print(f"값 '{value}'을(를) 변환하는 도중 오류가 발생했습니다: {e}")
            return value