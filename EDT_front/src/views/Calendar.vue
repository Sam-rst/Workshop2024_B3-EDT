<template>
    <ion-page>
      <ion-content>
        <div class="title-content">
            <div class="line-titlecontent"></div>
                <div>
                    <img src="/calendar2.png" alt="">
                </div>
                <div class="line-titlecontent"></div>
            </div>
        <div class="title-page">Vos prochains cours</div>
      </ion-content>
    </ion-page>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref } from 'vue';
  /*
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
  });*/
  </script>
  
  <style scoped>
  .title-content {
    text-align: center;
    text-transform: uppercase;
  }
  .line-titlecontent {
  width: 40%;
  height: 1px;
  background-color: #ffff;
}
.title-page {
  margin: 2% 0 2% 0;
  font-size: x-large; 
  text-transform: uppercase; 
  width: 100%; 
  text-align: center;
}
  </style>