from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.app.base.models.entities.base_entity import BaseEntity

class ClasseEntity(BaseEntity):
    __tablename__ = "classe"

    nom_formation = Column(String(255), nullable=False)
    annee_formation = Column(String(255), nullable=False)
    ecole = Column(String(255), nullable=False)

    created_by = Column(Integer, ForeignKey("user.id"), nullable=False)

    cours = relationship("ClasseEntity", back_populates="classe")