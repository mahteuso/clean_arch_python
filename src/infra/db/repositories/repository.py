from sqlalchemy import update, delete
from src.infra.db.settings.connection import DbConnectHandler as DB
from src.infra.db.entities.users import Users
from src.domain.models.users import Users as UsersModel
from typing import List


class UsersRepository:

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: str) -> None:
        with DB() as database:
            try:
                new_registry = Users(
                    first_name = first_name,
                    last_name = last_name,
                    age = age
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, first_name: str) -> List[UsersModel]:
        with DB() as database:
            try:
                users = (
                    database.session
                    .query(Users)
                    .filter(Users.first_name == first_name)
                    .all()
                )
                return users
            except Exception as exception:
                database.session.rollback()
                return exception

 