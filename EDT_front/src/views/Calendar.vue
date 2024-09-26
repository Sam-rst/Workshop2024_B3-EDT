<template>
    <Navbar />
    <ion-page>
      <ion-content>
        <div class="title-content">
            <div class="line-titlecontent"></div>
                <div>
                    <img src="/calendar2.png" alt="">
                </div>
                <div class="line-titlecontent"></div>
            </div>
        <div class="title-page">today</div>
      </ion-content>
    </ion-page>
  </template>
  
  <script lang="ts">
    import { defineComponent, ref } from 'vue';
    import Navbar from '@/components/Navbar.vue';
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