from sqlalchemy import Column, String, Integer, Date, Time, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.app.base.models.entities.base_entity import BaseEntity

class CoursEntity(BaseEntity):
    __tablename__ = "cours"

    nom = Column(String(255), nullable=False)
    jour = Column(Date, nullable=False)
    debut = Column(Time, nullable=False)
    fin = Column(Time, nullable=False)
    salle = Column(String(5), nullable=False)
    lieu = Column(String(255), nullable=False)
    commentaire = Column(String(255))
    en_distanciel = Column(Boolean, default=False)
    est_annule = Column(Boolean, default=False)
    en_learning = Column(Boolean, default=False)
    prof = Column(String(255), nullable=False)

    classe_id = Column(Integer, ForeignKey("classe.id"))
    classes = relationship("ClasseEntity", back_populates="cours")