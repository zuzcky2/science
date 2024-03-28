# 데이터베이스 패키지
이 패키지는 데이터베이스 모델 및 관련 기능을 제공하는 유틸리티 모음입니다. MongoDB를 기본으로 지원하며, Pydantic을 사용하여 데이터 모델링을 수행합니다.

### 기능
* MongoDB 모델 생성
* 데이터베이스 연결 관리
* 데이터베이스 질의 및 작업 수행
* 데이터베이스 마이그레이션

## 사용법
### MongoDB 모델 생성
```python
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

```

### 데이터베이스 연결 관리
```python
from app.packages.database import driver

# 드라이버 이름 가져오기
driver_name = config.get('database.default_driver')

# 드라이버 가져오기
db_driver = driver.get_driver(driver_name)

# 데이터베이스 연결
database_name = 'mlops'
db = db_driver.get_database(database_name)
```

### 데이터베이스 질의 및 작업 수행
```python
from app.models.account.user import UserModel

# UserModel 인스턴스 생성
user_model = UserModel()

# 사용자 추가
user_model.insert_one({'username': 'john', 'email': 'john@example.com'})

# 사용자 조회
user_model.find_one({'username': 'john'})
```

### 데이터베이스 마이그레이션
```python
from app.models.account.user import UserModel

# UserModel 인스턴스 생성
user_model = UserModel()

if user_model.has_migration:
    # 마이그레이션 생성
    user_model.migration_create()
    
    # 마이그레이션 삭제
    user_model.migration_delete()
    
    # 마이그레이션 재생성
    user_model.migration_recreate()
```

### 데이터베이스 팩토리
```python
from app.models.account.user import UserModel

# UserModel 인스턴스 생성
user_model = UserModel()

if user_model.has_factory:
    # 마이그레이션 생성
    user_model.factory_create()
```