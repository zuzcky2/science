from app.packages.database.src.model.mongodb_model import Model, Item, Items, Columns, Factories
from pydantic import Field
from typing import List
from pymongo import ASCENDING

class RoleModel(Model):
    """
    권한 모델 클래스입니다.

    Attributes:
        datetime (bool): 시간 정보 사용 여부를 나타내는 값입니다.
    """

    @property
    def collection_name(self) -> str:
        """
        컬렉션 이름을 반환하는 프로퍼티입니다.
        """
        return 'roles'

    datetime: bool = True

    class Item(Item):
        """
        권한 항목을 나타내는 내부 클래스입니다.
        """
        role_key: str = Field(..., title='권한 키', description='권한의 고유값', example='ROLE_GUEST')
        role_name: str = Field(..., title='권한 명칭', description='권한 식별 텍스트', example='손님')
        role_desc: str = Field(..., title='권한 설명', description='권한에 대한 설명', example='로그인 없이 방문한 회원')

    class Items(Items):
        """
        권한 항목 목록을 나타내는 내부 클래스입니다.

        Attributes:
            items (List['RoleModel.Item']): 권한 항목 목록입니다.
        """
        items: List['RoleModel.Item']

    @property
    def columns(self) -> Columns:
        """
        인덱스를 반환하는 프로퍼티입니다.
        """
        return Columns([{'value': [('role_key', ASCENDING)], 'unique': True}])

    @property
    def factories(self) -> Factories:
        """
        팩토리를 반환하는 프로퍼티입니다.
        """
        return Factories([
            {
                'value': self.Item(**{
                    'role_key': 'ROLE_GUEST',
                    'role_name': '손님',
                    'role_desc': '로그인하지 않은 방문한 사용자',
                }),
                'match': {
                    'role_key': 'ROLE_GUEST'
                }
            }, {
                'value': self.Item(**{
                    'role_key': 'ROLE_USER',
                    'role_name': '회원',
                    'role_desc': '로그인한 사용자',
                }),
                'match': {
                    'role_key': 'ROLE_USER'
                }
            }, {
                'value': self.Item(**{
                    'role_key': 'ROLE_ADMIN',
                    'role_name': '관리자',
                    'role_desc': '로그인한 관리자',
                }),
                'match': {
                    'role_key': 'ROLE_ADMIN'
                }
            }
        ])
