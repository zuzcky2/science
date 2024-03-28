import pymongo
from typing import Any, Optional, List, Union
from bson.objectid import ObjectId
from .model_abstract import ModelAbstract
from pydantic import BaseModel, Field
from abc import abstractmethod
from app.packages.database import connection
from app.packages.support import config
from app.packages.support.src.modules.kst import Kst


class PyObjectId(ObjectId):
    """
    MongoDB의 ObjectId에 대한 Pydantic 유효성 검사 및 수정을 담당하는 클래스입니다.
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("잘못된 objectid입니다.")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class MongoModel(BaseModel):
    """
    MongoDB 모델에 대한 Pydantic 기본 모델입니다.
    """

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ListModel(BaseModel):
    """
    목록을 나타내는 Pydantic 모델입니다.
    """
    items: List

    def __init__(self, data: List):
        super().__init__(items=data)

    def dict(self, *args, **kwargs):
        """
        모델을 딕셔너리로 변환합니다.
        """
        data = super().dict(*args, **kwargs)
        return data['items']


class Item(MongoModel):
    """
    MongoDB의 항목을 나타내는 Pydantic 모델입니다.
    """
    ObjectId: Optional[PyObjectId] = Field(None, title='MongoDB ObjectId')
    created_at: Optional[Kst]
    updated_at: Optional[Kst]
    deleted_at: Optional[Kst]


class Items(ListModel):
    """
    MongoDB의 항목 목록을 나타내는 Pydantic 모델입니다.
    """
    items: List[Item]


class Column(BaseModel):
    """
    인덱스를 나타내는 Pydantic 모델입니다.

    Attributes:
        value (List[tuple]): 인덱스 값입니다.
        unique (bool): 고유 여부를 나타내는 값입니다. 기본값은 False 입니다.
    """
    value: List[tuple]
    unique: bool = Field(False)


class Columns(Items):
    """
    인덱스 목록을 나타내는 Pydantic 모델입니다.

    Attributes:
        items (List[Column]): 인덱스 목록입니다.
    """
    items: List[Column]

    def __init__(self, data: List, datetime: bool = True):
        """
        인덱스 목록을 초기화합니다.

        Args:
            data (List): 인덱스 데이터입니다.
            datetime (bool, optional): 날짜 및 시간 필드를 자동으로 인덱싱할지 여부를 지정합니다. 기본값은 True 입니다.
        """
        if datetime:
            data = data + [
                {'value': [('created_at', pymongo.DESCENDING)], 'unique': False},
                {'value': [('updated_at', pymongo.DESCENDING)], 'unique': False},
                {'value': [('deleted_at', pymongo.DESCENDING)], 'unique': False}
            ]
        super().__init__(data=data)


class Factory(BaseModel):
    """
    팩토리를 나타내는 Pydantic 모델입니다.

    Attributes:
        value (Item): 생성할 항목입니다.
        match (Item): 기존 항목과 일치하는지 확인하기 위한 항목입니다.
    """
    value: Item
    match: Item


class Factories(ListModel):
    """
    팩토리 목록을 나타내는 Pydantic 모델입니다.

    Attributes:
        items (List[Factory]): 팩토리 목록입니다.
    """
    items: List[Factory]


class Model(ModelAbstract):
    """
    MongoDB 모델 클래스입니다.

    Attributes:
        __storage (Union[Item, Items, None]): 데이터 조회 결과 저장소
        __cursor (Optional[pymongo.cursor.Cursor]): 데이터 작업 결과 저장소
        datetime (bool): 날짜 자동화 사용 여부
    """

    __storage: Union[Item, Items, None] = None
    __cursor: Optional[pymongo.cursor.Cursor]

    Item: Item = Item
    Items: Items = Items

    datetime: bool = True

    @property
    def driver_name(self) -> str:
        """
        드라이버의 이름을 반환합니다.
        """
        return config.get('database.default_driver')

    @property
    def database_name(self) -> str:
        """
        데이터베이스의 이름을 반환합니다.
        """
        return 'mlops'

    @property
    @abstractmethod
    def collection_name(self) -> str:
        """
        컬렉션의 이름을 반환하는 추상 프로퍼티입니다.
        """
        pass

    @property
    @abstractmethod
    def columns(self) -> Columns:
        """
        마이그레이션 저장소
        """
        pass

    @property
    @abstractmethod
    def factories(self) -> Factories:
        """
        팩토리 목록 저장소
        """
        pass

    @property
    def has_migration(self):
        """
        마이그레이션이 있는지 확인합니다.
        """
        return True if self.columns else False

    @property
    def has_factory(self):
        """
        팩토리가 있는지 확인합니다.
        """
        return True if self.factories else False

    @property
    def driver(self) -> pymongo.mongo_client:
        """
        드라이버를 반환합니다.
        """
        if connection.default_driver == self.driver_name:
            return connection.driver
        else:
            return connection.get_driver(self.driver_name)

    @property
    def db(self) -> pymongo.mongo_client.database.Database:
        """
        데이터베이스를 반환합니다.
        """
        return self.driver.get_database(self.database_name)

    @property
    def col(self) -> pymongo.collection.Collection:
        """
        컬렉션을 반환합니다.
        """
        return self.db.get_collection(self.collection_name)

    @property
    def _storage(self) -> Union[Item, Items, None]:
        """
        저장소를 반환합니다.
        """
        return self.__storage

    @_storage.setter
    def _storage(self, storage: Union[Item, Items, None] = None):
        """
        저장소를 설정합니다.
        """
        self.__storage = storage

    @property
    def _cursor(self) -> pymongo.cursor.Cursor:
        """
        커서를 반환합니다.
        """
        return self.__cursor

    @_cursor.setter
    def _cursor(self, cursor: pymongo.cursor.Cursor):
        """
        커서를 설정합니다.
        """
        self.__cursor = cursor

    def dict(self):
        """
        저장소를 딕셔너리로 변환합니다.
        """
        return self._storage.dict() if self._storage else None

    def json(self):
        """
        저장소를 JSON 문자열로 변환합니다.
        """
        return self._storage.json() if self._storage else None

    ## MongoDB 작업
    def aggregate(self, *args, **kwargs: Any):
        """
        MongoDB 에서 집계 작업을 수행합니다.
        """
        self._storage = self.Items(list(self.col.aggregate(*args, **kwargs)))

    def aggregate_one(self, *args, **kwargs):
        """
        MongoDB 에서 단일 항목의 집계 작업을 수행합니다.
        """
        items = list(self.col.aggregate(*args, **kwargs))
        self._storage = self.Item(**items[0]) if len(items) > 0 else None

    def find_one(self, *args, **kwargs):
        """
        MongoDB 에서 단일 항목을 찾습니다.
        """
        item = self.col.find_one(*args, **kwargs)
        self._storage = self.Item(**item) if item else None

    def find(self, *args, **kwargs):
        """
        MongoDB 에서 항목을 찾습니다.
        """
        items = list(self.col.find(*args, **kwargs))
        self._storage = self.Item(**items[0]) if len(items) > 0 else None

    def insert_one(self, *args, **kwargs) -> pymongo.cursor.Cursor:
        """
        MongoDB 에 항목을 삽입합니다.
        """
        self._cursor = self.col.insert_one(*args, **kwargs)
        return self._cursor

    def insert_many(self, *args, **kwargs) -> pymongo.cursor.Cursor:
        """
        MongoDB 에 여러 항목을 삽입합니다.
        """
        self._cursor = self.col.insert_many(*args, **kwargs)
        return self._cursor

    def update_one(self, *args, **kwargs) -> pymongo.cursor.Cursor:
        """
        MongoDB 에서 항목을 업데이트합니다.
        """
        self._cursor = self.col.update_one(*args, **kwargs)
        return self._cursor

    def update_many(self, *args, **kwargs) -> pymongo.cursor.Cursor:
        """
        MongoDB 에서 여러 항목을 업데이트합니다.
        """
        self._cursor = self.col.update_many(*args, **kwargs)
        return self._cursor

    def delete_one(self, *args, **kwargs) -> pymongo.cursor.Cursor:
        """
        MongoDB 에서 항목을 삭제합니다.
        """
        self._cursor = self.col.delete_one(*args, **kwargs)
        return self._cursor

    def delete_many(self, *args, **kwargs) -> pymongo.cursor.Cursor:
        """
        MongoDB 에서 여러 항목을 삭제합니다.
        """
        self._cursor = self.col.delete_many(*args, **kwargs)

    def migration_create(self):
        """
        인덱스를 생성합니다.
        """
        if self.has_migration:
            for index in self.columns.items:
                self.col.create_index(index.value, unique=index.unique)

    def migration_delete(self):
        """
        컬렉션을 삭제합니다.
        """
        if self.has_migration:
            self.col.drop()

    def migration_recreate(self):
        """
        컬렉션을 재생성합니다.
        """
        self.migration_delete()
        self.migration_create()

    def factory_create(self):
        """
        팩토리를 생성합니다.
        """
        if self.has_factory:
            for factory in self.factories.items:
                data = factory.value.dict()
                now = Kst.now()
                if self.datetime:
                    data.update({
                        'created_at': now,
                        'updated_at': now,
                        'deleted_at': None
                    })

                self.col.update_one(factory.match.dict(), {'$set': data}, upsert=True)
