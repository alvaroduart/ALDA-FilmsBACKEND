from alda.domain.entities.user import User
from alda.domain.repositories.user_repository import UserRepository
from alda.domain.value_objects.email_vo import Email
from alda.domain.value_objects.password import Password


class LoginUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, email: Email, password: Password) -> User:
        user = self.repository.get_by_email(email)
        if not user:
            raise ValueError("User not found")
        
        if user.password.value() != password.value():
            raise ValueError("Invalid password")
        
        return user

