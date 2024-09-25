from src.app.user.repositories.user_repository import UserRepository
from src.app.user.models.dtos.user_dto import UserDTO



class UserService:
    
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def get_users(self) -> list[UserDTO]:
        return self.user_repository.get_users()

    def create_user(self, user: UserDTO):
        return self.user_repository.create_user(user)