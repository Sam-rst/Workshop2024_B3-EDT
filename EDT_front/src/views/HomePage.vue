<template>
  <ion-page>
    <Navbar />
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
          <ion-card-title class="card-title">VENDREDI 27/09</ion-card-title>
          <ion-card-subtitle class="card-subtitle">Workshop</ion-card-subtitle>
          <div class="lvl">B3 DEVIA FS ALT 24/25</div>
        </ion-card-header>

        <div>
          <div class="proff">Florian TOIX</div>
        </div>

        <div class="information">
          <div class="hours">
            <div class="start">08h00</div>
            <div class="end">12h00</div>
          </div>
          <div class="lieu">
            <div class="salle">Salle 001</div>
            <div class="typecours">(présentiel)</div>
          </div>
        </div>

      </ion-card>

      <ion-card class="card">
        <ion-card-header style="padding: 0;">
          <ion-card-title class="card-title">VENDREDI 27/09</ion-card-title>
          <ion-card-subtitle class="card-subtitle">Dev Python</ion-card-subtitle>
          <div class="lvl">B3 DEVIA FS ALT 24/25</div>
        </ion-card-header>

        <div>
          <div class="proff">Geoffroy LANDRAT</div>
        </div>

        <div class="information">
          <div class="hours">
            <div class="start">13h00</div>
            <div class="end">17h00</div>
          </div>
          <div class="lieu">
            <div class="salle">Salle 103</div>
            <div class="typecours">(présentiel)</div>
          </div>
        </div>


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
      <a class="button-calendar" href="/calendar">Emploi du temps</a>
    </div>
  </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import router from '@/router';
import { IonContent, IonHeader, IonPage, IonIcon, IonButton, IonTitle, IonToolbar } from '@ionic/vue';
import { ref } from "vue";
import { defineComponent } from 'vue';
import { personOutline } from 'ionicons/icons';
import Navbar from '@/components/Navbar.vue';

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
  background-color: #191919;
}
.card {
  width: 300px;
  max-width: 20%;
  background-color: #191919;
}
.card, .card-subtitle, .card-title {
  font-family: "DM Sans", sans-serif;
  color: white;
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
    border-top: 3333 solid 1px;
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
  margin: 5% 0;
}
.button-calendar {
  padding: 15px;
  border-radius: 5px;
  border: #191919 1px solid;
  color: black;
  font-size: large;
  text-decoration: none;
  font-family: "DM Sans", sans-serif;
}
.button-calendar:hover {
  background-color: #191919;
  color: white;
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