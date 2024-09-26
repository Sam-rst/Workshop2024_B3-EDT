import secrets, string, bcrypt
from fastapi import HTTPException
from src.transverse.emailSender import envoyerMailToUser
from src.app.base.repositories.base_repository import BaseRepository
from src.app.user.models.entities.user_entity import UserEntity
from src.app.user.models.dtos.user_dto import UserDTO
from src.app.base.services.utils_service import map_entity_dto_list

class UserRepository(BaseRepository):
    
    def get_users(self) -> list[UserDTO]:
        with self.session_factory() as session:
            users = session.query(UserEntity).all()
            users_dto = map_entity_dto_list(users, UserDTO)
        return users_dto

    def generate_password(self, firstname: str, lastname: str) -> str:
        # Définir les ensembles de caractères : majuscules, minuscules, chiffres et caractères spéciaux
        uppercase_letters = string.ascii_uppercase
        lowercase_letters = string.ascii_lowercase
        digits = string.digits
        special_chars = "!@#$%^&*()-_=+"

        # Générer au moins un caractère de chaque type
        password = [
            secrets.choice(uppercase_letters),  # Une majuscule
            secrets.choice(lowercase_letters),  # Une minuscule
            secrets.choice(digits),             # Un chiffre
            secrets.choice(special_chars)       # Un caractère spécial
        ]

        # Compléter le reste du mot de passe avec des caractères aléatoires
        # tout en ajoutant le prénom et le nom dans les 12 caractères minimum
        remaining_length = max(12 - len(firstname) - len(lastname), 4)
        password += [
            secrets.choice(uppercase_letters + lowercase_letters + digits + special_chars)
            for _ in range(remaining_length)
        ]

        # Ajouter le prénom et le nom (en limitant leur taille si nécessaire)
        password.append(firstname[:3].capitalize())  # Prendre les 3 premières lettres du prénom
        password.append(lastname[:3].capitalize())   # Prendre les 3 premières lettres du nom

        # Joindre les caractères pour obtenir une chaîne de mot de passe finale
        return ''.join(password)

    def create_user(self, user: UserDTO):
        try:
            with self.session_factory() as session:
                password = self.generate_password(user.firstname, user.lastname)
                password_hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                print(f"\n\n\nPassword: {password}\n\n\n")
                if not envoyerMailToUser(password=password, user_email=user.email, username=user.username):
                    raise HTTPException(status_code=422, detail="L'envoie du mail n'a pas fonctionné")
                
                new_user = UserEntity(
                    firstname=user.firstname,
                    lastname=user.lastname,
                    username=user.username,
                    email=user.email,
                    password=password_hashed,
                    classe_id=user.classe_id
                )
                
                session.add(new_user)
                session.flush()
                
                user_id = new_user.id
                session.commit()
                
                # Envoie du mail à l'utilisateur
                return {"id", user_id}
        except Exception as e:
            raise HTTPException(status_code=422, detail=e.args[0])

