from .user_finder_controller import UserFinderController
from src.data.tests.user_finder import UserFinderSpy

class HtttpRequestMock:
    def __init__(self) -> None:
        self.query_params = {"first_name" : "Mateus"}

def test_handle():
    http_request_mock = HtttpRequestMock()
    use_case = UserFinderSpy()
    user_finder_controller = UserFinderController(use_case)

    response = user_finder_controller.handle(http_request_mock)
    print()
    print(response.body)
    print(response.body["data"]["attributes"]["first_name"])

    assert response.body["data"]["attributes"]["first_name"] == http_request_mock.query_params["first_name"]
    assert response.status_code == 200
    
    

