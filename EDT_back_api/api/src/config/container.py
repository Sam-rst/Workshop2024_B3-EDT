from dependency_injector import containers, providers

from src.transverse.database import Database

from src.app.user.services.user_service import UserService
from src.app.user.repositories.user_repository import UserRepository

class Container(containers.DeclarativeContainer):
    
    URL_DATABASE = "postgresql://workshop2024_edt:workshop2024_edt@localhost:5432/workshop2024_edt"
    db = providers.Singleton(Database, db_url=URL_DATABASE)
    
    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)
    user_service = providers.Factory(UserService, user_repository=UserRepository)