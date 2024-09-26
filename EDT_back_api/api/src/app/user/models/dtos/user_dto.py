from datetime import datetime
from pydantic import BaseModel, Field
from src.app.user.models.entities.user_entity import UserEntity

class UserDTO(BaseModel):

    id: int = Field(description="Id de l'utilisateur")
    firstname: str = Field(description="Prénom de l'utilisateur")
    lastname: str = Field(description="Nom de famille de l'utilisateur")
    username: str = Field(description="Username de l'utilisateur")
    email: str = Field(description="Email de l'utilisateur")
    password: str = Field(description="Mot de passe hashé de l'utilisateur")
    role: int = Field(description="Rôle de l'utilisateur", default=1)

    classe_id: int = Field(description="Id de la classe")

    @classmethod
    def copy_from_entity(cls, user: UserEntity):
        return cls(
            id=user.id,
            firstname=user.firstname,
            lastname=user.lastname,
            username=user.username,
            email=user.email,
            password=user.password,
            role=user.role,
            created_at=user.created_at,
            updated_at=user.updated_at,
            classe_id=user.classe_id
        )
