# Projet Python - API avec FastAPI et PostgreSQL

## Description
Ce projet est une API développée avec **FastAPI** et utilise **PostgreSQL** comme base de données. L'objectif de ce projet est de [description de l'objectif du projet].

## Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés :
- [Python 3.8+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Git](https://git-scm.com/)

## Installation

Afin de garder les dépendances de votre projet isolées, il est recommandé de créer un environnement virtuel. Voici comment procéder :

### Packages python
- Sous **Windows** :
```bash
python -m venv env
./env/Scripts/activate
pip install -r requirements.txt
```

- Sous **Linux** et **MacOs** :
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### PostgreSQL
Si PostgreSQL n'est pas installé sur votre machine, vous pouvez l'installer en suivant les instructions suivantes :
1. Installation :
   - Windows : installer [PostgreSQL](https://www.postgresql.org/download/)

   - Linux :
    ```bash
    sudo apt install postgresql postgresql-contrib
    ```

    - MacOs :
    ```bash
    brew install postgresql
    brew services start postgresql
    ```

### Lancement
Une fois que tout a été réalisé jusqu'à maintenant, il ne manque plus qu'à lancer l'API :

```bash
cd api
uvicorn src.main:app --reload
```
