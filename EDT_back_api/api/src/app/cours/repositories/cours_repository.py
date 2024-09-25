from src.app.base.repositories.base_repository import BaseRepository
from src.app.cours.models.entities.cours_entity import CoursEntity
from src.app.cours.models.dtos.cours_dto import CoursDTO
from src.app.base.services.utils_service import map_entity_dto_list

class CoursRepository(BaseRepository):
    
    def get_cours(self) -> list[CoursDTO]:
        with self.session_factory() as session:
            cours = session.query(CoursEntity).all()
            cours_dto = map_entity_dto_list(cours, CoursDTO)
        return cours_dto