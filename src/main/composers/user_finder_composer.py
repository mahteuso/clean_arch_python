from src.infra.db.repositories.repository import UsersRepository
from src.data.use_cases.user_finder import UserFinder
from src.presentation.controllers.user_finder_controller import UserFinderController

def user_finder_compose():
    repo = UsersRepository()
    use_case = UserFinder(repo)
    controller = UserFinderController(use_case)

    return controller.handle
    