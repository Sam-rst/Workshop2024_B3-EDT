<!-- src/components/Navbar.vue -->
<template>
  <IonFooter>
      <div class="parent-header" style="width: 100%; text-align: center; font-size: xx-large; height: 100px; background-color: #191919; color: white">
      </div>
  </IonFooter>

</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { IonContent, IonFooter, IonTitle, IonToolbar } from '@ionic/vue';

export default defineComponent({
  name: 'Footer',
  components: {
    IonContent, IonFooter, IonTitle, IonToolbar
  }
});
</script>
<style scoped>
</style>