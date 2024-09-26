<template>
    <ion-page>


        <ion-content class="ion-padding">
            <div class="login-logo">
              <img src="/Logo_StudyTime.png" alt="logo study time">
            </div>
    
            <form novalidate expand="full" @submit.prevent="onLogin">
            <ion-list style="max-width: 45%; margin: auto;">
                <ion-item>
                <ion-input
                    label="Username"
                    labelPlacement="stacked"
                    v-model="username"
                    name="username"
                    type="text"
                    :spellcheck="false"
                    autocapitalize="off"
                    required
                ></ion-input>
                </ion-item>
    
                <ion-item>
                <ion-input
                    labelPlacement="stacked"
                    label="Password"
                    v-model="password"
                    name="password"
                    type="password"
                    required
                ></ion-input>
                </ion-item>
            </ion-list>
    
            <ion-row style="max-width: 45%; margin: auto;" responsive-sm class="ion-padding">
                <ion-col>
                  <ion-button :disabled="!canSubmit" type="submit" expand="block">Login</ion-button>
                </ion-col>
            </ion-row>
            </form>


            <ion-toast
            :is-open="showToast"
            :message="toastMessage"
            :duration="2000"
            ></ion-toast>
        </ion-content>
    </ion-page>
  </template>
  
  <style scoped>
  .login-logo {
    padding: 20px 0;
    min-height: 200px;
    text-align: center;
  }
  
  .login-logo img {
    max-width: 150px;
  }
  
  .list {
    margin-bottom: 0;
  }
  </style>
  
  <script setup lang="ts">
  import { computed, ref } from "vue";
  import {
    IonPage,
    IonHeader,
    IonToolbar,
    IonButtons,
    IonMenuButton,
    IonButton,
    IonContent,
    IonList,
    IonItem,
    IonTitle,
    IonRow,
    IonCol,
    IonInput,
    IonToast,
  } from "@ionic/vue";
  import router from '@/router';
  import Cookies from 'js-cookie';  
  
  const username = ref("");
  const password = ref("");
  const submitted = ref(false);
  
  const showToast = ref(false);
  const toastMessage = ref("");
  
  const canSubmit = computed(
    () => username.value.trim() !== "" && password.value.trim() !== ""
  );
  
  const onLogin = () => {
    submitted.value = true;
    //Vérifier si le username et le mot de passe sont correcte
    //username.value || password.value
    if (username.value === "student" && password.value === "password") {
        toastMessage.value = "Successfully logged in!";
        //Faire apparaitre le message en bas
        showToast.value = true;
        //set le nom du cookie et Contenue du cookie
        Cookies.set('user-session', 'session-token', { expires: 7 });
        const userCookie = Cookies.get('user-session');
        console.log(userCookie);
        router.push('/home');
    }
  };
  </script>