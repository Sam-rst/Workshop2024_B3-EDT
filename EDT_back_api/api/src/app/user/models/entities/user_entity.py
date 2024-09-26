from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.app.base.models.entities.base_entity import BaseEntity
from src.app.classe.models.entities.classe_entity import ClasseEntity

class UserEntity(BaseEntity):
    __tablename__ = "user"

    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Integer, default=1)  # 0: ADMIN - 1: USER

    classe_id = Column(Integer, ForeignKey("classe.id"))
    classes = relationship("ClasseEntity", back_populates="users")
