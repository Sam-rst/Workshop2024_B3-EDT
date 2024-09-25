<template>
    <ion-page>
      <ion-header>
        <ion-toolbar>
          <ion-title>Page À Propos</ion-title>
        </ion-toolbar>
      </ion-header>
      <ion-content>
        <div id="container">
          <form @submit.prevent="handleSubmit">
            <div>
              <label for="date">Date:</label>
              <input type="date" id="date" v-model="formData.date" required />
            </div>
            <div>
              <label for="heureDebut">Heure de début:</label>
              <input type="time" id="heureDebut" v-model="formData.heureDebut" required />
            </div>
            <div>
              <label for="heureFin">Heure de fin:</label>
              <input type="time" id="heureFin" v-model="formData.heureFin" required />
            </div>
            <div>
              <label for="salleClasse">Salle de classe:</label>
              <input type="text" id="salleClasse" v-model="formData.salleClasse" required />
            </div>
            <div>
              <label for="batiment">Bâtiment:</label>
              <input type="text" id="batiment" v-model="formData.batiment" required />
            </div>
            <div>
              <label for="cours">Type de cours:</label>
              <input type="text" id="cours" v-model="formData.cours" required />
            </div>
            <div>
              <label for="professeur">Professeur:</label>
              <input type="text" id="professeur" v-model="formData.professeur" required />
            </div>
            <button type="submit">{{ isEditing ? 'Modifier' : 'Soumettre' }}</button>
          </form>
          <h2>Créneaux ajoutés:</h2>
          <ul>
            <li v-for="(creneau, index) in creneaux" :key="index">
              {{ creneau.date }} - {{ creneau.heureDebut }} à {{ creneau.heureFin }} : {{ creneau.cours }} avec {{ creneau.professeur }} en {{ creneau.salleClasse }} ({{ creneau.batiment }})
              <button @click="editCreneau(index)">Modifier</button>
              <button @click="deleteCreneau(index)">Supprimer</button>
            </li>
          </ul>
          <pre>{{ jsonData }}</pre>
        </div>
      </ion-content>
    </ion-page>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref } from 'vue';
  
  export default defineComponent({
    name: 'AboutPage',
    setup() {
      const formData = ref({
        date: '',
        heureDebut: '',
        heureFin: '',
        salleClasse: '',
        batiment: '',
        cours: '',
        professeur: ''
      });
  
      const creneaux = ref<Array<any>>([]);
      const jsonData = ref('');
      const isEditing = ref(false);
      const editIndex = ref<number | null>(null);
  
      const handleSubmit = () => {
        if (isEditing.value && editIndex.value !== null) {
          creneaux.value[editIndex.value] = { ...formData.value };
          isEditing.value = false;
          editIndex.value = null;
        } else {
          creneaux.value.push({ ...formData.value });
        }
  
        formData.value.heureDebut = '';
        formData.value.heureFin = '';
        formData.value.salleClasse = '';
        formData.value.batiment = '';
        formData.value.cours = '';
        formData.value.professeur = '';
  
        jsonData.value = JSON.stringify(creneaux.value, null, 2);
      };
  
      const editCreneau = (index: number) => {
        formData.value = { ...creneaux.value[index] };
        isEditing.value = true;
        editIndex.value = index;
      };
  
      const deleteCreneau = (index: number) => {
        creneaux.value.splice(index, 1);
        jsonData.value = JSON.stringify(creneaux.value, null, 2);
      };
  
      return {
        formData,
        creneaux,
        jsonData,
        isEditing,
        editIndex,
        handleSubmit,
        editCreneau,
        deleteCreneau
      };
    }
  });
  </script>
  
  <style scoped>
  #container {
    text-align: center;
    padding: 20px;
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