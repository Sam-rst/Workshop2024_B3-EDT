from contextlib import contextmanager, AbstractContextManager
from typing import Callable, Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, scoped_session, sessionmaker

Base = declarative_base()

class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=False)
        self._session_factory = scoped_session(sessionmaker(
            autoflush=False,
            bind=self._engine
        ))
    
    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)
    
    @contextmanager
    def session(self) -> Generator[Session, None, None]:
    # def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise ValueError("La session a rollback à cause de des exceptions")
        finally:
            session.close()