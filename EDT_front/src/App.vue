<template>
  <ion-app>
    <ion-router-outlet />
  </ion-app>
</template>

<script lang="ts">
import { IonApp, IonRouterOutlet } from '@ionic/vue';
import Navbar from './components/Navbar.vue';
import { computed } from 'vue';
import { useRoute } from 'vue-router';

export default {
  components: {
    IonApp,
    IonRouterOutlet,
  },
  
  setup() {
    const route = useRoute();
    
    // Log pour voir le nom de la route actuelle

    // Utilise computed pour déterminer si la Navbar doit s'afficher
    const shouldShowNavbar = computed(() => {
      return route.name !== 'Login'; // Condition inverse
    });

    return {
      shouldShowNavbar
    };
  }
}
</script>
