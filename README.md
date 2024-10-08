# Workshop2024 - Mobile & Web App Project

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Ionic](https://img.shields.io/badge/Ionic-Framework-green)](https://ionicframework.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.0-brightgreen)](https://vuejs.org/)

Workshop2024 est une application mobile et web multiplateforme développée pour gérer et consulter les horaires de cours d'une école. Cette application offre une interface intuitive et réactive, permettant aux utilisateurs de recevoir les horaires à jour chaque soir.

## 🚀 Fonctionnalités principales

- ✅ **Notification quotidienne des horaires** : Recevez chaque soir les horaires du lendemain directement sur votre appareil.
- 📅 **Affichage des cours** : Consultez vos horaires par jour, semaine ou mois.
- 🔑 **Authentification sécurisée** : Utilisation de tokens JWT pour une authentification rapide et sécurisée.
- 🔄 **Synchronisation en temps réel** : Horaires mis à jour automatiquement via une API.
- 📲 **Disponible sur mobile et web** : Compatible avec les appareils Android et iOS, ainsi que sur navigateur.

## 📱 Captures d'écran

| Accueil                           | Horaires de la semaine              | Notifications                       |
|------------------------------------|-------------------------------------|-------------------------------------|
| ![Accueil](docs/screenshots/home.png) | ![Horaires](docs/screenshots/schedule.png) | ![Notifications](docs/screenshots/notifications.png) |

## 🛠️ Technologies utilisées

- **Frontend** : [Ionic Framework](https://ionicframework.com/), [Vue.js](https://vuejs.org/)
- **Backend** : [FastAPI](https://fastapi.tiangolo.com/), [PostgreSQL](https://www.postgresql.org/)
- **Authentification** : JWT (JSON Web Tokens)
- **Gestion des données** : SQLAlchemy pour la base de données
- **Notifications** : Firebase Cloud Messaging (FCM)
- **SMTP** : Outlook

## 📦 Installation du projet

Suivez ces étapes pour installer et lancer le projet en local.

### Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- [Node.js](https://nodejs.org/) (version 14.x ou supérieure)
- [Ionic CLI](https://ionicframework.com/docs/cli) installé globalement
- [Python 3.9+](https://www.python.org/) pour le backend
- [PostgreSQL](https://www.postgresql.org/) pour la base de données

### Installation du répertoire

1. Clonez le dépôt du projet :

   ```bash
   git clone https://github.com/votre-utilisateur/workshop2024.git
    ```
2. Suivre les instructions de l'[installation du back/api](EDT_back_api/README.md)

3. Suivre les instructions de l'[installation du front](EDT_front/README.md)