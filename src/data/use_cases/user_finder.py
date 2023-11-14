from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from typing import Dict
from src.data.interfaces.users_repository import UsersRepositoryInterface


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository
            

    def find(self, first_name: str) -> Dict:
        
        if not first_name.isalpha():
            raise Exception('Nome inválido para busca')

        if len(first_name) > 18:
            raise Exception('Nome muito grande para busca')

        users = self.__users_repository.select_user(first_name)
        if users == []:
            raise Exception("Usuário não encontrado")

        response = {
            "type": "Users",
            "count": len(users),
            "attributes": users
        }

        return response

