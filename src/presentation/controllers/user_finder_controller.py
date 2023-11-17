from src.presentation.interface.controller_interface import ControllerInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.presentation.http_types.http_reponse import HttpResponse
from src.presentation.http_types.httP_request import HttpRequest



class UserFinderController(ControllerInterface):
    def __init__(self, user_case: UserFinderInterface ) -> None:
        self.__user_case = user_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.query_params["first_name"]

        response = self.__user_case.find(first_name)

        return HttpResponse(
            status_code = 200,
            body = {"data": response}
        )