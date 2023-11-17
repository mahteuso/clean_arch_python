from src.presentation.controllers.user_register_controller import UserRegisterController as User
from src.data.tests.user_register import UserRegisterSpy

class HtttpRequestMock:
    def __init__(self) -> None:
        self.body = {
            "first_name": "Mateus",
            "last_name": "Laranjeira",
            "age": 42
        }

def test_handle():
    http_request_mock = HtttpRequestMock()
    use_case = UserRegisterSpy()
    user_register_controller = User(use_case)

    response = user_register_controller.handle(http_request_mock)

    # assert response.body["data"]["attributes"]["first_name"] == http_request_mock.body["first_name"]
    # assert response.body["data"]["attributes"]["last_name"] == http_request_mock.body["last_name"]
    # assert response.body["data"]["attributes"]["age"] == http_request_mock.body["age"]