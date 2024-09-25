from fastapi import APIRouter, status
from src.routers.user_router import user_router

main_router = APIRouter()

@main_router.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message": "Hello World"}
    # return JSONResponse(status_code=status.HTTP_200_OK, content="Hello World")

main_router.include_router(user_router)