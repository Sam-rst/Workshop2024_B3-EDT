from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.app.base.models.entities.base_entity import BaseEntity
from src.app.cours.models.entities.cours_entity import CoursEntity

class ClasseEntity(BaseEntity):
    __tablename__ = "classe"

    nom_formation = Column(String(255), nullable=False)
    annee_formation = Column(String(255), nullable=False)
    ecole = Column(String(255), nullable=False)

    users = relationship("UserEntity", back_populates="classes")
    cours = relationship("CoursEntity", back_populates="classes")