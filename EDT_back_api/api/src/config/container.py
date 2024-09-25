from dependency_injector import containers, providers

from src.transverse.database import Database

from src.app.auth.services.auth_service import AuthService
from src.app.user.services.user_service import UserService
from src.app.user.repositories.user_repository import UserRepository
from src.app.classe.services.classe_service import ClasseService
from src.app.classe.repositories.classe_repository import ClasseRepository
from src.app.cours.services.cours_service import CoursService
from src.app.cours.repositories.cours_repository import CoursRepository

class Container(containers.DeclarativeContainer):
    
    wiring_config = containers.WiringConfiguration(packages=["..routers"])
    
    URL_DATABASE = "postgresql://postgres:postgres@localhost:5432/workshop2024_edt"
    db = providers.Singleton(Database, db_url=URL_DATABASE)
    session_factory = providers.Callable(db.provided.session)
    
    
    user_repository = providers.Factory(UserRepository, session_factory=session_factory)
    user_service = providers.Factory(UserService, user_repository=user_repository)
    auth_service = providers.Factory(AuthService, user_repository=user_repository)
    
    classe_repository = providers.Factory(ClasseRepository, session_factory=session_factory)
    classe_service = providers.Factory(ClasseService, classe_repository=classe_repository)
    
    cours_repository = providers.Factory(CoursRepository, session_factory=session_factory)
    cours_service = providers.Factory(CoursService, cours_repository=cours_repository)