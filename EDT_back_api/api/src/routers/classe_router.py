from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.app.classe.services.classe_service import ClasseService

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