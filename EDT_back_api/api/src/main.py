import os
from fastapi import FastAPI
from dotenv import load_dotenv

from src.config.generate_secret_key import generate_and_store_secret_key

from src.routers.main_router import main_router
from src.config.container import Container

load_dotenv()

container = Container()
container.init_resources()

def create_app() -> FastAPI:
    
    generate_and_store_secret_key()
    
    db = container.db()
    db.create_database()

    app = FastAPI(
        docs_url="/api",
        openapi_url="/api/openapi.json"
    )
    app.container = container
    app.include_router(main_router)
    
    return app

app = create_app()