from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from src.app.base.models.entities.base_entity import BaseEntity

class CoursEntity(BaseEntity):
    __tablename__ = "cours"

    debut = Column(DateTime, nullable=False)
    fin = Column(DateTime, nullable=False)
    salle = Column(String(5), nullable=False)
    lieu = Column(String(255), nullable=False)
    commentaire = Column(String(255))
    en_distanciel = Column(Boolean, default=False)
    prof = Column(String(255), nullable=False)

    classe = Column(Integer, ForeignKey("classe.id"), nullable=False)