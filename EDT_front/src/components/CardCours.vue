<template>
    <div class="parent-cards">
      <ion-card v-for="cour in cours" :key="cour.id" class="card">
        <ion-card-header style="padding: 0;">
          <ion-card-title class="card-title">{{ cour.jour }}</ion-card-title>
          <ion-card-subtitle class="card-subtitle">{{ cour.nom }}</ion-card-subtitle>
          <div class="lvl">B3 DevOps Orienté IA 2024-2025</div>
        </ion-card-header>
  
        <div>
          <div class="proff">{{ cour.prof }}</div>
        </div>
  
        <div class="information">
          <div class="hours">
            <div class="start">{{ formatTime(cour.debut) }}</div>
            <div class="end">{{ formatTime(cour.fin) }}</div>
          </div>
          <div class="lieu">
            <div class="salle">{{ cour.salle }}</div>
            <div class="typecours" v-if="cour.en_distanciel">(Distanciel)</div>
            <div class="typecours" v-else>(Présentiel)</div>
          </div>
        </div>
      </ion-card>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        cours: [],
      };
    },
    mounted() {
      this.refresh();
    },
    methods: {
      async refresh() {
        try {
          const response = await fetch("http://samrst.fr:8000/cours/prochains_cours");
          const data = await response.json();
          this.cours = data;
          console.log(this.cours)
        } catch (error) {
          console.error("Erreur lors de la récupération des cours :", error);
        }
      },
      formatTime(timeArray) {
        // Cette fonction formate [HH, MM] en "HHhMM"
        const [hour, minute] = timeArray;
        return `${String(hour).padStart(2, "0")}h${String(minute).padStart(2, "0")}`;
      },
    },
  };
  </script>
  
  <style scoped></style>
  