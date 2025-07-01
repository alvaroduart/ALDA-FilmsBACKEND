from alda.domain.entities.user import User
from alda.domain.repositories.user_repository import UserRepository
from alda.domain.value_objects.email_vo import Email
from alda.domain.value_objects.password import Password


class RegisterUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, user: User) -> User:
        # Verificar se o email já existe
        try:
            existing_user = self.repository.get_by_email(user.email.value())
            if existing_user:
                raise ValueError("Email already exists")
        except:
            pass  # Email não existe, pode prosseguir
        
        self.repository.create(user)
        return user

