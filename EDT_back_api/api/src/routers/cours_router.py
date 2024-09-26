from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from dependency_injector.wiring import Provide, inject

from src.app.cours.services.cours_service import CoursService
from src.app.cours.models.dtos.cours_dto import CoursDTO
from src.config.container import Container

cours_router = APIRouter(
    prefix="/cours",
    tags=["cours"],
    responses={
        status.HTTP_200_OK: {"message": "Success"},
        status.HTTP_201_CREATED: {"message": "Le cours a bien été créé"},
        status.HTTP_404_NOT_FOUND: {"message": "Page introuvable"},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"message": "Erreur de validation des données entrantes"},
    }
)

@cours_router.get(
    "",
    response_description="Récupération des cours",
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK
)
@inject
def route_get_cours(request: Request,
          cours_service: CoursService = Depends(Provide[Container.cours_service])
        ) -> JSONResponse:
    """
    <li>Récupération des cours</li>
    <li>Args :
    
    </li>
    <li>Returns : 
        JSONResponse: Liste des cours
    </li>
    """
    cours_dtos = cours_service.get_cours()
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(cours_dtos)
    )

@cours_router.get(
    "/prochains_cours",
    response_description="Récupération des cours du lendemain",
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK
)
@inject
def route_get_prochains_cours(request: Request,
          cours_service: CoursService = Depends(Provide[Container.cours_service])
        ) -> JSONResponse:
    """
    <li>Récupération des prochains cours de la journée de cours la plus proche de l'heure de la requête</li>
    <li>Args :
    
    </li>
    <li>Returns : 
        JSONResponse: List[Cours]
    </li>
    """
    cours_dtos = cours_service.get_prochains_cours()
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(cours_dtos)
    )

@cours_router.post(
    "/create",
    response_description="Création d'un cours",
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED
)
@inject
def create_cours(
    cours: CoursDTO,
    cours_service: CoursService = Depends(Provide[Container.cours_service])
    ) -> JSONResponse:
    
    output_response = cours_service.create_cours(cours)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(output_response)
    )