from datetime import date, time
from pydantic import BaseModel, Field
from src.app.cours.models.entities.cours_entity import CoursEntity

class CoursDTO(BaseModel):

    id: int = Field(description="Id du cours")
    nom: str = Field(description="Nom du cours")
    jour: date = Field(description="Le jour du cours")
    debut: tuple[int, int] = Field(description="Tuple de l'heure et minute du début du cours sous forme (HH, MM)", default=(8,0))
    fin: tuple[int, int] = Field(description="Tuple de l'heure et minute de la fin du cours sous forme (HH, MM)", default=(10,0))
    salle: str = Field(description="Salle de l'établissement dans lequel se fera le cours", default="110")
    lieu: str = Field(description="Lieu de l'établissement dans lequel se fera le cours", default="Rue Lucien Faure, Bordeaux")
    commentaire: str = Field(description="Description du cours vide ou non")
    en_distanciel: bool = Field(description="Si le cours est en distanciel", default=False)
    est_annule: bool = Field(description="Si le cours est annulé", default=False)
    en_learning: bool = Field(description="Si le cours est en learning", default=False)
    prof: str = Field(description="Nom du prof")
    
    classe_id: int = Field(description="Id de la classe")

    @classmethod
    def copy_from_entity(cls, entity: CoursEntity):
        return cls(
            id=entity.id,
            nom=entity.nom,
            jour=entity.jour,
            debut=(entity.debut.hour, entity.debut.minute),  # Récupérer heure et minute pour debut
            fin=(entity.fin.hour, entity.fin.minute),        # Récupérer heure et minute pour fin
            salle=entity.salle,
            lieu=entity.lieu,
            commentaire=entity.commentaire,
            en_distanciel=entity.en_distanciel,
            est_annule=entity.est_annule,
            en_learning=entity.en_learning,
            prof=entity.prof,
            classe_id=entity.classe_id
        )
