import os
import secrets
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

def generate_and_store_secret_key():
    """Génère et stocke la clé secrète dans le fichier .env si elle n'existe pas."""
    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        secret_key = secrets.token_hex(32)  # Génère une clé secrète de 64 caractères hexadécimaux
        with open('.env', 'a') as env_file:  # Ajoute la clé secrète dans le fichier .env
            env_file.write(f'SECRET_KEY={secret_key}\n')
    return secret_key