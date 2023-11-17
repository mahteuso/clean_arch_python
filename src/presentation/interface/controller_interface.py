from abc import ABC, abstractmethod
from src.presentation.http_types.http_reponse import HttpResponse
from src.presentation.http_types.httP_request import HttpRequest

class ControllerInterface(ABC):
    
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse: ...