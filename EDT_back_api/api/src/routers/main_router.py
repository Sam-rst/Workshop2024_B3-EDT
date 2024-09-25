from fastapi import APIRouter, status
from src.routers.auth_router import auth_router
from src.routers.user_router import user_router
from src.routers.classe_router import classe_router
from src.routers.cours_router import cours_router

main_router = APIRouter()

@main_router.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message": "Hello World"}
    # return JSONResponse(status_code=status.HTTP_200_OK, content="Hello World")

main_router.include_router(auth_router)
main_router.include_router(user_router)
main_router.include_router(classe_router)
main_router.include_router(cours_router)