from fastapi import HTTPException
from datetime import datetime

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

    def create_classe(self, classe: ClasseDTO):
        try:
            with self.session_factory() as session:
                new_classe = ClasseEntity(
                    nom_formation=classe.nom_formation,
                    annee_formation=classe.annee_formation,
                    ecole=classe.ecole,
                    created_at=datetime.now(),
                    updated_at=datetime.now()
                )
                
                session.add(new_classe)
                session.flush()
                
                classe_id = new_classe.id
                session.commit()
                return {"id", classe_id}
        except Exception as e:
            raise HTTPException(status_code=422, detail=e.args[0])