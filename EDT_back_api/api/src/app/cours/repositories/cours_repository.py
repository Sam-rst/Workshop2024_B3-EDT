from sqlalchemy import asc, cast, Date
from datetime import datetime

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

    def get_prochains_cours(self) -> list[CoursDTO]:
        with self.session_factory() as session:
            cours_proche = (
            session.query(CoursEntity)
            .filter(CoursEntity.debut > datetime.now())
            .order_by(asc(CoursEntity.debut))
            .first()
            )
            
            if not cours_proche:
                return []  # Si aucun cours trouvé on renvoie une liste vide

            date_proche = cours_proche.debut.date()

            cours_du_meme_jour = (
            session.query(CoursEntity)
            .filter(cast(CoursEntity.debut, Date) == date_proche)
            .order_by(asc(CoursEntity.debut))
            .all()
            )

            # Convertir les entités en DTO
            cours_dto = [CoursDTO.copy_from_entity(cours) for cours in cours_du_meme_jour]
        return cours_dto