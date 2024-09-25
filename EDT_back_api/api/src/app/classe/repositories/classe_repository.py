from src.app.base.repositories.base_repository import BaseRepository
from src.app.classe.models.dtos.classe_dto import ClasseDTO

class ClasseRepository(BaseRepository):
    
    def get_classes(self) -> list[ClasseDTO]:
        pass