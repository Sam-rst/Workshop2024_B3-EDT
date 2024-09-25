from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, BigInteger, String, DateTime, Boolean

Base = declarative_base()

class BaseEntity(Base):
    
    __abstract__ = True
    
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)