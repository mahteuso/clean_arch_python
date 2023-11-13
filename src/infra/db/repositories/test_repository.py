from .repository import UsersRepository
from sqlalchemy import text
from src.infra.db.settings.connection import DbConnectHandler
import pytest

db_connect_handler = DbConnectHandler()
engine = db_connect_handler.engine
conn = engine.connect()

@pytest.mark.skip(reason="Sensitive test")
def test_insert_user():
    mocked_first_name = 'Marco'
    mocked_last_name = 'Maria'
    mocked_age = 40

    user = UsersRepository()
    user.insert_user(mocked_first_name, mocked_last_name, mocked_age)

    sql = f'''
        SELECT * FROM users
        WHERE first_name = '{mocked_first_name}'
        AND last_name = '{mocked_last_name}'
        AND AGE = {mocked_age}
    '''
    response = conn.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

@pytest.mark.skip(reason="Sensitive test")
def test_select_user():
    mocked_first_name = 'Mateus'
    mocked_last_name = 'Laranjeira'
    mocked_age = 42

    sql = f'''
        INSERT INTO users (first_name, last_name, age)
        VALUES ('{mocked_first_name}', '{mocked_last_name}', '{mocked_age}')
    '''
    conn.execute(text(sql))
    conn.commit()

    user = UsersRepository()
    response = user.select_user(mocked_first_name)
    for registry in response:
        if registry.first_name == mocked_first_name:
            assert registry.first_name == mocked_first_name
            assert registry.last_name == mocked_last_name
            assert registry.age == mocked_age
            print(registry)