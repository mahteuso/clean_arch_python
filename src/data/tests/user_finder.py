from typing import Dict

class UserFinderSpy:

    def __init__(self) -> None:
        self.__user_attributes = {}

    def find(self, first_name: str) -> Dict:
        self.__user_attributes["first_name"] = first_name

        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "first_name": first_name,
                "last_name": "last_name",
                "age": 42
            }
        }

        return response
