from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from dependency_injector.wiring import Provide, inject

from src.app.user.services.user_service import UserService
from src.app.user.models.dtos.user_dto import UserDTO
from src.config.container import Container

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={
        status.HTTP_200_OK: {"message": "Success"},
        status.HTTP_201_CREATED: {"message": "L'utilisateur a bien été créé"},
        status.HTTP_404_NOT_FOUND: {"message": "Page introuvable"},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"message": "Erreur de validation des données entrantes"},
    }
)

@user_router.get(
    "",
    response_description="Récupération des users",
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK
)
@inject
def route_get_users(request: Request,
          user_service: UserService = Depends(Provide[Container.user_service])
        ) -> JSONResponse:
    """
    <li>Récupération des users</li>
    <li>Args :
    
    </li>
    <li>Returns : 
        JSONResponse: Liste des users
    </li>
    """
    user_dtos = user_service.get_users()
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(user_dtos)
    )

@user_router.post(
    "/create",
    response_description="Création d'un user",
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED
)
@inject
def create_user(
    user: UserDTO,
    user_service: UserService = Depends(Provide[Container.user_service])
    ) -> JSONResponse:
    
    output_response = user_service.create_user(user)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(output_response)
    )