from src.app.cours.repositories.cours_repository import CoursRepository
from src.app.cours.models.dtos.cours_dto import CoursDTO



class CoursService:
    
    def __init__(self, cours_repository: CoursRepository):
        self.cours_repository = cours_repository
    
    def get_cours(self) -> list[CoursDTO]:
        return self.cours_repository.get_cours()

    def get_prochains_cours(self) -> list[CoursDTO]:
        return self.cours_repository.get_prochains_cours()
    
    def create_cours(self, cours: CoursDTO):
        return self.cours_repository.create_cours(cours)