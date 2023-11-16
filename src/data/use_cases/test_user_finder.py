from .user_finder import UserFinder
from src.infra.db.tests.users_repository import UsersRepositorySpy

def test_find():
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    mocked_first_name = 'Rogério'

    result = user_finder.find(mocked_first_name)

    assert repo.select_user_attributes["first_name"] == mocked_first_name 
    assert result["type"] == "Users"
    assert result["count"] == len(result["attributes"])
    assert result["attributes"] != []

    print()
    print(result)
     


def test_find_error_in_invalid_name():
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    mocked_first_name = 'Rogério123'

    try:
        user_finder.find(mocked_first_name)
        assert False
    except Exception as exception:
        assert str(exception) == 'Nome inválido para busca'

def test_find_error_in_too_long_name():
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    mocked_first_name = 'RogérioMariaMateusLaranjeira'

    try:
        user_finder.find(mocked_first_name)
        assert False
    except Exception as exception:
        assert str(exception) == 'Nome muito grande para busca'

def test_find_error_user_not_found():
    class UsersRepositoryError(UsersRepositorySpy):
        def select_user(self, first_name: str):
            return []

    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)

    mocked_first_name = 'Mateus'

    try:
        user_finder.find(mocked_first_name)
        assert False
    except Exception as exception:
        assert str(exception) == 'Usuário não encontrado'

    