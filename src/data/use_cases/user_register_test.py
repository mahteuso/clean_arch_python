from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_register import UserRegister

def test_register():

    mocked_first_name = 'Mateus'
    mocked_last_name = 'Maranhão'
    mocked_age = 45

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)
    response = user_register.register(mocked_first_name, mocked_last_name, mocked_age)

    print(response)

    assert response["type"] == 'Users'
    assert response["count"] == 1
    assert response["attributes"]["first_name"] == mocked_first_name
    assert response["attributes"]["last_name"] == mocked_last_name
    assert response["attributes"]["age"] == mocked_age

    assert repo.insert_user_attributes["first_name"] == mocked_first_name
    assert repo.insert_user_attributes["last_name"] == mocked_last_name
    assert repo.insert_user_attributes["age"] == mocked_age

def test_first_name_error():

    mocked_first_name = 'Mateus123'
    mocked_last_name = 'Maranhão'
    mocked_age = 45

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)
    
    try:
        user_register.register(mocked_first_name, mocked_last_name, mocked_age)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome inválido para busca"
