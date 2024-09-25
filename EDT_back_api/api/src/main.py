from fastapi import FastAPI

from src.routers.main_router import main_router
from src.config.container import Container

container = Container()
container.init_resources()

def create_app() -> FastAPI:
    
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