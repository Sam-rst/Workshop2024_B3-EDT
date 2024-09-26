from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from dependency_injector.wiring import Provide, inject

from src.app.classe.services.classe_service import ClasseService
from src.app.classe.models.dtos.classe_dto import ClasseDTO
from src.config.container import Container

classe_router = APIRouter(
    prefix="/classes",
    tags=["classes"],
    responses={
        status.HTTP_200_OK: {"message": "Succès"},
        status.HTTP_201_CREATED: {"message": "La classe a bien été créee"},
        status.HTTP_404_NOT_FOUND: {"message": "Page introuvable"},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"message": "Erreur de validation des données entrantes"},
    }
)



@classe_router.get(
    "",
    response_description="Récupération des cours",
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK
)
@inject
def route_get_classes(request: Request,
          classe_service: ClasseService = Depends(Provide[Container.classe_service])
        ) -> JSONResponse:
    """
    <li>Récupération des classes</li>
    <li>Args :
    
    </li>
    <li>Returns : 
        JSONResponse: Liste des classes
    </li>
    """
    classes_dtos = classe_service.get_classes()
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(classes_dtos)
    )

@classe_router.post(
    "/create",
    response_description="Création d'une classe",
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED
)
@inject
def create_classe(
    classe: ClasseDTO,
    classe_service: ClasseService = Depends(Provide[Container.classe_service])
    ) -> JSONResponse:
    
    output_response = classe_service.create_classe(classe)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(output_response)
    )
