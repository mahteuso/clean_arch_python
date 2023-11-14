class Users:

    def __init__(self, id: int, first_name: str, last_name: str, age: int) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def __repr__(self):
        return f"id = {self.id}, first_name = {self.first_name}, last_name = {self.last_name}"