from fastapi import APIRouter
from src.routers.user_router import user_router

main_router = APIRouter()

main_router.include_router(user_router)