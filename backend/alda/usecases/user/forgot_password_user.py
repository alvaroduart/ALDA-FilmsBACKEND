from alda.domain.entities.user import User
from alda.domain.repositories.user_repository import UserRepository
from alda.domain.value_objects.email_vo import Email
from alda.domain.value_objects.password import Password


class ForgotPasswordUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, email: Email) -> None:
        user = self.repository.get_by_email(email)
        if not user:
            raise ValueError("User with this email does not exist")
        self.repository.forgot_password(email)

