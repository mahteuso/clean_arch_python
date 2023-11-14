from src.domain.models.users import Users as UsersModel
from typing import List

class UsersRepositorySpy:

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert_user(self, first_name: str, last_name: str, age: str) -> None:
        self.insert_user_attributes["first_name"] = first_name
        self.insert_user_attributes["last_name"] = last_name
        self.insert_user_attributes["age"] = age
        

    def select_user(self, first_name: str) -> List[UsersModel]:
        self.select_user_attributes["first_name"] = first_name
        return [
            UsersModel(10, first_name, 'Laranjeira', 42),
            UsersModel(13, first_name, 'Pereira', 40),
            UsersModel(40, first_name, 'Maria', 57)
        ]
