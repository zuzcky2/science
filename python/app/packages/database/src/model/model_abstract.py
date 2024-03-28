from abc import ABC, abstractmethod

class ModelAbstract(ABC):
    """
    추상 드라이버 클래스입니다.
    """

    @abstractmethod
    def find_one(self, *args, **kwargs):
        """
        단일 문서를 검색합니다.
        """
        pass

    @abstractmethod
    def find(self, *args, **kwargs):
        """
        여러 문서를 검색합니다.
        """
        pass

    @abstractmethod
    def insert_one(self, *args, **kwargs):
        """
        단일 문서를 삽입합니다.
        """
        pass

    @abstractmethod
    def insert_many(self, *args, **kwargs):
        """
        여러 문서를 삽입합니다.
        """
        pass

    @abstractmethod
    def update_one(self, *args, **kwargs):
        """
        단일 문서를 업데이트합니다.
        """
        pass

    @abstractmethod
    def update_many(self, *args, **kwargs):
        """
        여러 문서를 업데이트합니다.
        """
        pass

    @abstractmethod
    def delete_one(self, *args, **kwargs):
        """
        단일 문서를 삭제합니다.
        """
        pass

    @abstractmethod
    def delete_many(self, *args, **kwargs):
        """
        여러 문서를 삭제합니다.
        """
        pass

    @abstractmethod
    def migration_create(self):
        """
        데이터베이스에 데이터를 생성하는 추상 메서드입니다.
        """
        pass

    @abstractmethod
    def migration_delete(self):
        """
        데이터베이스에서 데이터를 삭제하는 추상 메서드입니다.
        """
        pass

    def migration_recreate(self):
        """
        데이터베이스에 데이터를 다시 생성하는 메서드입니다.
        """
        self.migration_delete()
        self.migration_create()