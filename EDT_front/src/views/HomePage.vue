<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Connexion</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content>
      <div id="container">
        <form @submit.prevent="handleLogin">
          <div>
            <label for="username">Nom d'utilisateur:</label>
            <input type="text" id="username" v-model="username" required />
          </div>
          <div>
            <label for="password">Mot de passe:</label>
            <input type="password" id="password" v-model="password" required />
          </div>
          <button type="submit">Se connecter</button>
        </form>
        <p>Si vous n'avez pas de compte, veuillez contacter un administrateur à l'adresse suivante : <a href="mailto:admin@example.com">admin@example.com</a></p>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/vue';

const username = ref('');
const password = ref('');

const handleLogin = () => {
  // Logic for handling login
  console.log('Nom d\'utilisateur:', username.value);
  console.log('Mot de passe:', password.value);
};
</script>

<style scoped>
#container {
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
}

#container div {
  margin-bottom: 16px;
}

#container label {
  display: block;
  margin-bottom: 8px;
  font-size: 16px;
}

#container input {
  width: 100%;
  padding: 8px;
  font-size: 16px;
  margin-bottom: 8px;
}

#container button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

#container p {
  font-size: 16px;
  line-height: 22px;
  color: #8c8c8c;
  margin: 0;
}

#container a {
  text-decoration: none;
  color: #007bff;
}
</style>