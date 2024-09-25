from src.app.base.repositories.base_repository import BaseRepository
from src.app.user.models.entities.user_entity import UserEntity
from src.app.user.models.dtos.user_dto import UserDTO
from src.app.base.services.utils_service import map_entity_dto_list

class UserRepository(BaseRepository):
    
    def get_users(self) -> list[UserDTO]:
        with self.session_factory() as session:
            users = session.query(UserEntity).all()
            users_dto = map_entity_dto_list(users, UserDTO)
        return users_dto