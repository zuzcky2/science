from app.packages.database.src.model.mongodb_model import Model, Item, Items, Columns, Factories, PyObjectId
from pydantic import Field, EmailStr
from typing import List
from pymongo import ASCENDING, DESCENDING

class UserModel(Model):
    """
    회원 모델 클래스입니다.

    Attributes:
        datetime (bool): 시간 정보 사용 여부를 나타내는 값입니다.
    """

    @property
    def collection_name(self) -> str:
        """
        컬렉션 이름을 반환하는 프로퍼티입니다.
        """
        return 'users'

    datetime: bool = True

    class Item(Item):
        """
        유저 항목을 나타내는 내부 클래스입니다.
        """
        email: EmailStr = Field(..., title='이메일 주소', description='사용자 이메일', example='example@gmail.com')
        password: str = Field(..., min_length=8, max_length=128, title='비밀번호', description='사용자 비밀번호')
        role_id: PyObjectId = Field(title='권한 ID')

    class Items(Items):
        """
        유저 항목 목록을 나타내는 내부 클래스입니다.

        Attributes:
            items (List['UserModel.Item']): 유저 항목 목록입니다.
        """
        items: List['UserModel.Item']

    @property
    def columns(self) -> Columns:
        """
        인덱스를 반환하는 프로퍼티입니다.
        """
        return Columns([
            {'value': [('email', ASCENDING)], 'unique': True},
            {'value': [('role_id', ASCENDING)], 'unique': False},
            {'value': [('created_at', DESCENDING)], 'unique': False},
            {'value': [('updated_at', DESCENDING)], 'unique': False},
            {'value': [('deleted_at', DESCENDING)], 'unique': False},
        ])

    @property
    def factories(self) -> Factories:
        """
        팩토리를 반환하는 프로퍼티입니다.
        """
        return Factories([
            {
                'value': self.Item(**{
                    'email': 'jjambbongjoa@gmail.com',
                    'password': '1234qwer',
                    'role_id': 1,
                }),
                'match': {
                    'email': 'jjambbongjoa@gmail.com'
                }
            }
        ])
