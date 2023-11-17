from src.presentation.interface.controller_interface import ControllerInterface
from src.domain.use_cases.use_register import UserRegister as UserRegisterInterface
from src.presentation.http_types.http_reponse import HttpResponse
from src.presentation.http_types.httP_request import HttpRequest


class UserRegisterController(ControllerInterface):
    def __init__(self, user_case: UserRegisterInterface ) -> None:
        self.__user_case = user_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.body["first_name"]
        last_name = http_request.body["last_name"]
        age = http_request.body["age"]

        response = self.__user_case.register(first_name, last_name, age)

        return HttpResponse(
            status_code = 200,
            body = {"data": response}
        )