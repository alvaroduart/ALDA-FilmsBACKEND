from alda.domain.entities.user import User
from alda.domain.repositories.user_repository import UserRepository


class LogoutUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, user_id: str) -> None:
        """
        Logs out the user by their ID.
        
        :param user_id: The ID of the user to log out.
        """
        self.repository.logout(user_id)
