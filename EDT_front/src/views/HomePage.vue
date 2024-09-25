<template>

    <ion-header>
      <ion-toolbar style="padding: 0 30px 0 30px;">
        <ion-title slot="start"><img src="/Logo_StudyTime_white.png" width="100px" alt="logo study time"></ion-title>
        <div slot="end" class="group-icon">
          <a id="icon-header" href="/home"><img src="/home-outline.svg" alt="logo profil"></a>
          <a id="icon-header" href="/calendar"><img src="/calendar-number-outline.svg" alt="logo profil"></a>
          <a id="icon-header" href="/profil"><img src="/person-circle-outline.svg" alt="logo profil"></a>
        </div>
        <ion-title>Study Time</ion-title>
      </ion-toolbar>
    </ion-header>

    <div class="title-content">
      <h1>Vos prochains cours</h1>
    </div>

    <div class="parent-cards">
        <ion-card class="card">
        <ion-card-header>
          <ion-card-title class="card-title">MERCREDI 25/06</ion-card-title>
          <ion-card-subtitle class="card-subtitle">Cours de ...</ion-card-subtitle>
          <div class="lvl">B3 DEVIA FS ALT 24/25</div>
        </ion-card-header>

        <div class="line"></div>

        <div>
          <div class="proff">Jambor Veronika</div>
        </div>

        <div class="line"></div>   
        
        <div class="information">
          <div class="hours">
            <div class="start">09h00</div>
            <div class="end">10h00</div>
          </div>
          <div class="horizontal-line"></div>
          <div class="lieu">
            <div class="salle">Salle 103</div>
            <div class="typecours">(distanciel)</div>
          </div>
        </div>

        <ion-button fill="clear" @click="Action">Modifier</ion-button>
      </ion-card>

      <ion-card class="card">
        <ion-card-header>
          <ion-card-title class="card-title">MERCREDI 25/06</ion-card-title>
          <ion-card-subtitle class="card-subtitle">Cours de ...</ion-card-subtitle>
        </ion-card-header>

        <ion-button fill="clear" @click="Action">Modifier</ion-button>
      </ion-card>
    </div>
</template>

<script setup lang="ts">
import router from '@/router';
import { IonContent, IonHeader, IonPage, IonIcon, IonButton, IonTitle, IonToolbar } from '@ionic/vue';
import { ref } from "vue";
import { defineComponent } from 'vue';
import { personOutline } from 'ionicons/icons';

const Action = () => {
  router.push("/admin")
};
</script>

<style scoped>
.group-icon a {
  margin: 10px;
}
.group-icon a img {
  width: 30px; 
  fill: white;
}
.group-icon a img:hover {
  transform: scale(1.1);
}
.title-content {
  text-align: center;
  text-transform: uppercase;
}
.parent-cards {
  display: flex;
  justify-content: space-evenly;
}
.line {
  width: 100%;
  height: 1px;
  background-color: #ffff;
}
.horizontal-line {
  width: 1px;
  height: 100%;
  background-color: #ffff;
}
.card {
  max-width: 30%;
}
.card-title {
  text-transform: uppercase;
}
.card-subtitle {
  text-transform: uppercase;
}
</style>