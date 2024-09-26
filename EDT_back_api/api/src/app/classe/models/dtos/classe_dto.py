from datetime import datetime
from pydantic import BaseModel, Field
from src.app.classe.models.entities.classe_entity import ClasseEntity
from src.app.user.models.dtos.user_dto import UserDTO
from src.app.cours.models.dtos.cours_dto import CoursDTO

class ClasseDTO(BaseModel):
    
    id: int = Field(description="Id de la classe")
    nom_formation: str = Field(description="Nom de la formation de la classe")
    annee_formation: str = Field(description="Année de formation de la classe (ex: 'B1', 'B2', 'M1', etc...)")
    ecole: str = Field(description="Nom de l'école dans laquelle la classe se trouve")

    users: list[UserDTO] = []
    cours: list[CoursDTO] = []

    @classmethod
    def copy_from_entity(cls, entity: ClasseEntity):
        return cls(
            id=entity.id,
            nom_formation=entity.nom_formation,
            annee_formation=entity.annee_formation,
            ecole=entity.ecole,
            users=[UserDTO.copy_from_entity(user) for user in entity.users],
            cours=[CoursDTO.copy_from_entity(cour) for cour in entity.cours]
        )
