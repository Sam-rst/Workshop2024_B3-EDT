from datetime import datetime
from pydantic import BaseModel, Field
from src.app.user.models.entities.user_entity import UserEntity
from src.app.classe.models.dtos.classe_dto import ClasseDTO

class UserDTO(BaseModel):

    id: int = Field(description="Id de l'utilisateur")
    firstname: str = Field(description="Prénom de l'utilisateur")
    lastname: str = Field(description="Nom de famille de l'utilisateur")
    username: str = Field(description="Username de l'utilisateur")
    email: str = Field(description="Email de l'utilisateur")
    password: str = Field(description="Mot de passe hashé de l'utilisateur")
    role: int = Field(description="Rôle de l'utilisateur", default=1)
    created_at: datetime = Field(description="L'utilisateur a été créé tel jour", default=datetime.now())
    updated_at: datetime = Field(description="L'utilisateur a été modifié tel jour")

    #classes_created ne peut être modifié que par l'administrateur
    classes_created: list[ClasseDTO] = Field(description="Classes créées par l'administrateur (INFO : doit être créé que quand le rôle est 0 --ADMIN--)", default=[])

    @classmethod
    def copy_from_entity(cls, entity: UserEntity):

        return cls(
            id=entity.id,
            firstname=entity.firstname,
            lastname=entity.lastname,
            username=entity.username,
            email=entity.email,
            password=entity.password,
            role=entity.role,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            classes_created=[ClasseDTO.copy_from_entity(classe) for classe in entity.classes_created]
            )