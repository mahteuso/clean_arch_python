from typing import Dict

class UserRegisterSpy:

    def __init__(self) -> None:
        self.user_attributes = {}

    def register(self, first_name: str, last_name: str, age: int ) -> Dict:
        self.user_attributes["first_name"] = first_name
        self.user_attributes["last_name"] = last_name
        self.user_attributes["age"] = age
        
        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age
            } 
        }
        return response