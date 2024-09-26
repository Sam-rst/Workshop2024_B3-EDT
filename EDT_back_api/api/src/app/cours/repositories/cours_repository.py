from sqlalchemy import asc, cast, Date
from datetime import datetime
from fastapi import HTTPException

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
    
    def create_cours(self, cours: CoursDTO):
        try:
            with self.session_factory() as session:
                debut = f"{cours.debut[0]}:{cours.debut[1]}:00"
                fin = f"{cours.fin[0]}:{cours.fin[1]}:00"
                
                new_cours = CoursEntity(
                    nom=cours.nom,
                    jour=cours.jour,
                    debut=debut,
                    fin=fin,
                    salle=cours.salle,
                    lieu=cours.lieu,
                    commentaire=cours.commentaire,
                    en_distanciel=cours.en_distanciel,
                    est_annule=cours.est_annule,
                    en_learning=cours.en_learning,
                    prof=cours.prof,
                    classe_id=cours.classe_id
                )
                
                session.add(new_cours)
                session.flush()
                
                cours_id = cours.id
                session.commit()
                return {"id", cours_id}
        except Exception as e:
            raise HTTPException(status_code=422, detail=e.args[0])

    def get_prochains_cours(self) -> list[CoursDTO]:
        with self.session_factory() as session:
            cours_proche = (
            session.query(CoursEntity)
            .filter(CoursEntity.jour > datetime.now().date())
            .order_by(asc(CoursEntity.debut))
            .first()
            )
            
            if not cours_proche:
                return []  # Si aucun cours trouvé on renvoie une liste vide

            cours_du_meme_jour = (
            session.query(CoursEntity)
            .filter(CoursEntity.jour == cours_proche.jour)
            .order_by(asc(CoursEntity.debut))
            .all()
            )

            # Convertir les entités en DTO
            cours_dto = [CoursDTO.copy_from_entity(cours) for cours in cours_du_meme_jour]
        return cours_dto