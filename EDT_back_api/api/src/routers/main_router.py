from fastapi import APIRouter
from user_router import user_router

main_router = APIRouter()

main_router.include_router(user_router)