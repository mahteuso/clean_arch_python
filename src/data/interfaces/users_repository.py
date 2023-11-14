from abc import ABC, abstractmethod
from typing import List
from src.domain.models.users import Users as UsersModel

class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(cls, first_name: str, last_name: str, age: str) -> None: ...

    @abstractmethod
    def select_user(cls, first_name: str) -> List[UsersModel]: ...
