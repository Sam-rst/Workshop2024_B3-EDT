from datetime import datetime
from pydantic import BaseModel, Field
from src.app.classe.models.entities.classe_entity import ClasseEntity

class ClasseDTO(BaseModel):
    id: int = Field(description="Id de la classe")
    nom_formation: str = Field(description="Nom de la formation de la classe")
    annee_formation: str = Field(description="Année de formation de la classe (ex: 'B1', 'B2', 'M1', etc...)")
    ecole: str = Field(description="Nom de l'école dans laquelle la classe se trouve")
    created_at: datetime = Field(description="La classe a été créée tel jour", default_factory=datetime.now)
    updated_at: datetime = Field(description="La classe a été modifiée tel jour", default_factory=datetime.now)
    created_by: int = Field(description="L'ID de l'utilisateur qui a créé la classe")

    @classmethod
    def copy_from_entity(cls, entity: ClasseEntity):
        return cls(
            id=entity.id,
            nom_formation=entity.nom_formation,
            annee_formation=entity.annee_formation,
            ecole=entity.ecole,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            created_by=entity.created_by
        )
