<template>
  <ion-content>
    <div class="title-content">
      <div class="line-titlecontent"></div>
      <div>
        <img src="/horloge.png" alt="">
      </div>
      <div class="line-titlecontent"></div>
    </div>
    <div class="title-page">Vos prochains cours</div>

    <div class="parent-cards">
      <ion-card class="card">
        <ion-card-header style="padding: 0;">
          <ion-card-title class="card-title">MERCREDI 25/06</ion-card-title>
          <ion-card-subtitle class="card-subtitle">Dev Python Learning</ion-card-subtitle>
          <div class="lvl">B3 DEVIA FS ALT 24/25</div>
        </ion-card-header>

        <div>
          <div class="proff">Jambor Veronika</div>
        </div>

        <div class="information">
          <div class="hours">
            <div class="start">09h00</div>
            <div class="end">10h00</div>
          </div>
          <div class="lieu">
            <div class="salle">Salle 103</div>
            <div class="typecours">(distanciel)</div>
          </div>
        </div>

        <ion-button fill="clear" style="text-align: center; width: 100%;" @click="Action">Modifier</ion-button>
      </ion-card>

      <ion-card class="card">
        <ion-card-header style="padding: 0;">
          <ion-card-title class="card-title">MERCREDI 25/06</ion-card-title>
          <ion-card-subtitle class="card-subtitle">Dev Python Learning</ion-card-subtitle>
          <div class="lvl">B3 DEVIA FS ALT 24/25</div>
        </ion-card-header>

        <div>
          <div class="proff">Jambor Veronika</div>
        </div>

        <div class="information">
          <div class="hours">
            <div class="start">09h00</div>
            <div class="end">10h00</div>
          </div>
          <div class="lieu">
            <div class="salle">Salle 103</div>
            <div class="typecours">(distanciel)</div>
          </div>
        </div>

        <ion-button fill="clear" style="text-align: center; width: 100%;" @click="Action">Modifier</ion-button>
      </ion-card>
    </div>

    <div class="title-content">
      <div class="line-titlecontent"></div>
      <div>
        <img src="/agenda.png" alt="">
      </div>
      <div class="line-titlecontent"></div>
    </div>
    <div class="title-page">Visualiser l’emploi du temps</div>

    <div class="parent-button-caldendar">
      <a class="button-calendar" href="/calendat">Emploi du temps</a>
    </div>
  </ion-content>
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
body, html, ion-content {
  height: 100%;
  overflow: auto;
}

/*.group-icon a {
  margin: 10px;
}
.group-icon a img {
  width: 30px; 
  fill: white;
}
.group-icon a img:hover {
  transform: scale(1.1);
}*/
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
.title-page {
  margin: 2% 0 2% 0;
  font-size: x-large; 
  text-transform: uppercase; 
  width: 100%; 
  text-align: center;
}
.title-content {
  margin-top: 3%;
  display: flex;
    align-items: center;
    justify-content: space-between;
}
.line-titlecontent {
  width: 40%;
  height: 1px;
  background-color: #ffff;
}
.card {
  max-width: 20%;
}
.card, .card-subtitle, .card-title {
  font-family: "DM Sans", sans-serif;
  color: #ffff;
}
.card-title {
  text-transform: uppercase;
  padding: 5%;
  font-size: x-large;
  text-align: center;
}
.card-subtitle {
  text-transform: uppercase;
  font-size: xx-large;
    text-align: center;
    border-top: white solid 1px;
    padding: 7%;
}
.lvl {
  text-align: end;
}
.proff {
  text-align: center;
    font-size: x-large;
    padding: 7%;
    border-top: #ffff solid 1px;
}
.information {
  display: flex;
  justify-content: space-around;
  align-items: center;
}
.hours {
  width: 100%;
  height: 100%;
  text-align: center;
  border-right: 1px solid white;
  border-top: 1px solid white;
  padding-top: 5%;
}
.hours div:nth-child(2) {
  margin-top: 15%;
}
.lieu {
  width: 100%;
  text-align: center;
  border-top: 1px solid white;
  padding-top: 5%;
}
.lieu div:nth-child(2) {
  margin-top: 15%;
}
.parent-button-caldendar {
  text-align: center;
  margin-top: 5%;
}
.button-calendar {
  padding: 15px;
  border-radius: 5px;
  border: white 1px solid;
  color: white;
  font-size: large;
  text-decoration: none;
  font-family: "DM Sans", sans-serif;
}
.button-calendar:hover {
  background-color: #ffff;
  color: black;
}
@media (min-width: 1200px) {
  .card-subtitle {
    font-size: large;
  }
  .card {
    max-width: 100%;
  }
}
@media (min-width: 576px) and (max-width: 1199px) {
  .card-subtitle {
    font-size: medium;
  }
  .card {
    max-width: 100%;
  }
}
@media (max-width: 575px) {
  .card-subtitle {
    font-size: medium;
  }
  .card {
    max-width: 100%;
  }
  .parent-cards {
    display: grid;
  }
  .parent-button-caldendar {
    margin-top: 15%;
  }
}

</style>