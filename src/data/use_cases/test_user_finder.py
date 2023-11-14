from .user_finder import UserFinder
from src.infra.db.tests.users_repository import UsersRepositorySpy

def test_find():
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    mocked_first_name = 'Rogério'
    mocked_last_name = 'Laranjeira'
    mocked_age = 42

    result = user_finder.find(mocked_first_name)
    print(result)
    print()
    print(len(result["attributes"]))
    print()


    assert result["type"] == "Users"
    assert result["count"] == len(result["attributes"])
    assert result["attributes"] != []


