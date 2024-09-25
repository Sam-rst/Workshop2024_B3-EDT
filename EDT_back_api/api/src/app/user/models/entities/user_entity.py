from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.app.base.models.entities.base_entity import BaseEntity

class UserEntity(BaseEntity):
    __tablename__ = "user"

    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    username = Column(String(255), unique=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Integer, default=1) # 0: ADMIN - 1: USER

    classes_created = relationship("ClasseEntity", back_populates="created_by")