from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from dependency_injector.wiring import Provide, inject

from src.app.auth.services.auth_service import AuthService
from src.config.container import Container

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={
        status.HTTP_200_OK: {"message": "Success"},
        status.HTTP_404_NOT_FOUND: {"message": "Page introuvable"},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"message": "Erreur de validation des données entrantes"},
    }
)

@auth_router.post(
    "/login",
    response_description="Connexion au compte",
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
    status_code=status.HTTP_200_OK
)
@inject
def login(form_data: OAuth2PasswordRequestForm = Depends(), auth_service: AuthService = Depends(Provide[Container.auth_service])):
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = auth_service.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}