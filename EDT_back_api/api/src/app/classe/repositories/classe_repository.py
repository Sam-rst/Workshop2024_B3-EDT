from src.app.base.repositories.base_repository import BaseRepository
from src.app.classe.models.entities.classe_entity import ClasseEntity
from src.app.classe.models.dtos.classe_dto import ClasseDTO
from src.app.base.services.utils_service import map_entity_dto_list

class ClasseRepository(BaseRepository):
    
    def get_classes(self) -> list[ClasseDTO]:
        with self.session_factory() as session:
            classes = session.query(ClasseEntity).all()
            classes_dto = map_entity_dto_list(classes, ClasseDTO)
        return classes_dto