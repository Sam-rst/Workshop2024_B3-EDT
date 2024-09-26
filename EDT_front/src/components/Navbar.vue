<!-- src/components/Navbar.vue -->
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

</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { IonHeader, IonToolbar, IonTitle } from '@ionic/vue';

export default defineComponent({
  name: 'Navbar',
  components: {
    IonHeader,
    IonToolbar,
    IonTitle
  }
});
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