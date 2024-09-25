from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.app.base.models.entities.base_entity import BaseEntity
from src.app.cours.models.entities.cours_entity import CoursEntity

class ClasseEntity(BaseEntity):
    __tablename__ = "classe"

    nom_formation = Column(String(255), nullable=False)
    annee_formation = Column(String(255), nullable=False)
    ecole = Column(String(255), nullable=False)

    created_by = Column(Integer, ForeignKey("user.id"), nullable=False)
    users = relationship("UserEntity", back_populates="classes_created", foreign_keys=[created_by])  # Ajout de foreign_keys
    cours = relationship("CoursEntity", back_populates="classes", foreign_keys=[CoursEntity.classe_id])  # Ajout de foreign_keys
