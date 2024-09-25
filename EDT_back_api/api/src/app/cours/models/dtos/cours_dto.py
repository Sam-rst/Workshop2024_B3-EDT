from datetime import datetime
from pydantic import BaseModel, Field
from src.app.cours.models.entities.cours_entity import CoursEntity
from src.app.classe.models.dtos.classe_dto import ClasseDTO

class CoursDTO(BaseModel):

    id: int = Field(description="Id du cours")
    debut : datetime = Field(description="Date et heure du début du cours sous forme de datetime : 'YYYY-MM-DDTHH:MM:SS'")
    fin : datetime = Field(description="Date et heure du début du cours sous forme de datetime : 'YYYY-MM-DDTHH:MM:SS'")
    salle: str = Field(description="Salle de l'établissement dans lequel se fera le cours")
    lieu: str = Field(description="Lieu de l'établissement dans lequel se fera le cours")
    commentaire: str = Field(description="Description du cours vide ou non")
    created_at: datetime = Field(description="Le cours a été créé tel jour", default=datetime.now())
    updated_at: datetime = Field(description="Le cours a été modifié tel jour")

    classe: ClasseDTO = Field(description="Le cours appartient à telle classe")

    @classmethod
    def copy_from_entity(cls, entity: CoursEntity):
        
        return cls(
            id=entity.id,
            debut=entity.debut,
            fin=entity.fin,
            salle=entity.salle,
            lieu=entity.lieu,
            commentaire=entity.commentaire,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            classe=ClasseDTO.copy_from_entity(entity.classe)
            )