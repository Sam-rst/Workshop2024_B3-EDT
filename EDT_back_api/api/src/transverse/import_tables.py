from src.transverse.database import Base, Database
from src.app.user.models.entities.user_entity import UserEntity
from src.app.classe.models.entities.classe_entity import ClasseEntity
from src.app.cours.models.entities.cours_entity import CoursEntity

db = Database("postgresql://workshop2024_edt:workshop2024_edt@localhost:5432/workshop2024_edt")
Base.metadata.create_all(db._engine)
