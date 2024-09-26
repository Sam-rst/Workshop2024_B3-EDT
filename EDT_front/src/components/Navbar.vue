<!-- src/components/Navbar.vue -->
<template>
  <ion-header style="background-color: white; color: black;">
      <div class="parent-header">
        <div>
          <img src="/Logo_StudyTime.png" width="100px" alt="logo study time">
        </div>
        <div class="today-date">
          {{ today }}
        </div>
        <div class="group-icon">
          <a id="icon-header" href="/home"><img src="/home2.png" alt="logo profil"></a>
          <a id="icon-header" href="/calendar"><img src="/calendar-number-outline.svg" alt="logo profil"></a>
          <a id="icon-header" href="/profil"><img src="/person-circle-outline.svg" alt="logo profil"></a>
        </div>
      </div>
  </ion-header>

</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { IonHeader, IonToolbar, IonTitle } from '@ionic/vue';

export default defineComponent({
  name: 'Navbar',
  components: {
    IonHeader,
    IonToolbar,
    IonTitle,
  },
  setup() {
    // Fonction pour obtenir la date formatée
    const formatDate = (date: Date): string => {
      return date.toLocaleDateString('fr-FR', {
        weekday: 'long',
        day: 'numeric',
        month: 'long',
      });
    };

    // Créer une date et la formater
    const today = ref<string>(formatDate(new Date()));

    // Renvoyer les variables réactives pour le template
    return { today };
  },
});
</script>
<style scoped>
body {
  background-color: white;
}
.today-date {
  font-size: x-large;
  font-family: "DM Sans", sans-serif;
  text-transform: uppercase;
}
.parent-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.group-icon a {
  margin: 10px;
}
.group-icon a img {
  width: 30px; 
}
.group-icon a img:hover {
  transform: scale(1.1);
}
</style>