from src.app.classe.repositories.classe_repository import ClasseRepository
from src.app.classe.models.dtos.classe_dto import ClasseDTO



class ClasseService:
    
    def __init__(self, classe_repository: ClasseRepository):
        self.classe_repository = classe_repository
    
    def get_classes(self) -> list[ClasseDTO]:
        return self.classe_repository.get_classes()

    def create_classe(self, classe: ClasseDTO):
        return self.classe_repository.create_classe(classe)