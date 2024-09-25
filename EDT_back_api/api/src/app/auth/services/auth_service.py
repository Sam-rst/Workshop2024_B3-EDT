import os
from datetime import timedelta, datetime
from jose import jwt
from passlib.context import CryptContext
from src.app.user.repositories.user_repository import UserRepository
from src.app.user.models.dtos.user_dto import UserDTO

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def authenticate_user(self, username: str, password: str):
        user = self.user_repository.get_by_username(username)
        if user and self.verify_password(password, user.password):
            return user
        return None

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def create_user(self, signup_data: dict):
        hashed_password = self.hash_password(signup_data["password"])
        signup_data["password"] = hashed_password
        user_dto = UserDTO(**signup_data)
        return self.user_repository.create(user_dto)

    def verify_password(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)

    def hash_password(self, password: str):
        return pwd_context.hash(password)
