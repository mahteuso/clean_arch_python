class UsersRepository:

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: str) -> None:
        with DBConnectHandler() as database:
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
    def select_user(cls, first_name: str) -> any:
        with DbConnectHandler() as database:
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

    @classmethod
    def update_user(cls, first_name: str, last_name: str) -> any:
        with DbConnectHandler() as database:
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

    @classmethod
    def delete_user(cls, id: int) -> None:
        with DbConnectHandler() as database:
            try:
                _find = database.session.get(User, id)
                database.session.delete(_find)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception