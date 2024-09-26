<template>
    <ion-page>
        <Navbar />
        <ion-content>
            <div class="title-content">
                <div class="line-titlecontent"></div>
                <div>
                <img src="/calendar2.png" alt="">
                </div>
                <div class="line-titlecontent"></div>
            </div>

            <div class="parent-header-title">
                <a :href="`/calendar?date=${firstDateNature}`"><img src="/fleche.png" alt=""></a>
                <div class="title-page">{{ firstDate }} / {{ lastDate }}</div>
                <a :href="`/calendar?date=${lastDateNature}`"><img style="transform: rotate(180deg)" src="/fleche.png" alt=""></a>
            </div>

            <div>
                <ul class="parent-calendar">
                    
                <div class="hours">
                    <div style="padding: 9px;background-color: black;">ㅤ</div>
                    <div class="hour-left"><p>8h</p></div>
                    <div class="hour-left"><p>9h</p></div>
                    <div class="hour-left"><p>10h</p></div>
                    <div class="hour-left"><p>12h</p></div>
                    <div class="hour-left"><p>13h</p></div>
                    <div class="hour-left"><p>14h</p></div>
                    <div class="hour-left"><p>15h</p></div>
                    <div class="hour-left"><p>16h</p></div>
                    <div class="hour-left"><p>17h</p></div>
                </div>
                    <li v-for="date in dates" :key="date">
                        <div class="hours">
                            <p class="date">{{ date }}</p>
                            <div class="content-hour"><p class="content" id="1"></p></div>
                            <div class="content-hour"><p class="content" id="2"></p></div>
                            <div class="content-hour"><p class="content" id="3"></p></div>
                            <div class="content-hour"><p class="content" id="4"></p></div>
                            <div class="content-hour"><p class="content" id="5"></p></div>
                            <div class="content-hour"><p class="content" id="6"></p></div>
                            <div class="content-hour"><p class="content" id="7"></p></div>
                            <div class="content-hour"><p class="content" id="8"></p></div>
                            <div class="content-hour"><p class="content" id="9"></p></div>
                        </div>
                    </li>
                </ul>
            </div>
        </ion-content>
    </ion-page>
  </template>
  
  <script lang="ts">
  import { IonContent, IonPage } from '@ionic/vue';
  import { defineComponent, ref, onMounted } from 'vue';
  import Navbar from '@/components/Navbar.vue';
  import { useRoute } from 'vue-router';

  export default defineComponent({
    name: 'Calendar',
    setup() {
        const dates = ref<string[]>([]);
        const firstDateNature = ref<string | null>(null); 
        const firstDate = ref<string | null>(null); 
        const lastDateNature = ref<string | null>(null);  
        const lastDate = ref<string | null>(null);   
        const route = useRoute();

        const parseDate = (dateString: string) => {
            const [day, month, year] = dateString.split('/').map(Number);
            return new Date(year, month - 1, day);
        };

        const formatDate = (date: Date) => {
            const day = String(date.getDate()).padStart(2, '0');
            const month = String(date.getMonth() + 1).padStart(2, '0'); 
            const year = date.getFullYear();
            return `${day}/${month}/${year}`;
        };

        const getCurrentWeekDates = (startDate: Date) => {
            const weekDates = [];
            const dayOfWeek = startDate.getDay(); 

            const firstDayOfWeek = new Date(startDate);
            firstDayOfWeek.setDate(startDate.getDate() - dayOfWeek + 1);

            for (let i = 0; i < 7; i++) {
                const date = new Date(firstDayOfWeek);
                date.setDate(firstDayOfWeek.getDate() + i);
                weekDates.push(date);
            }

            return weekDates;
        };

        const initializeDates = () => {
            const queryDate = route.query.date as string;
            const currentDate = new Date();

            const formatDateB = (date: Date) => {
                return date.toLocaleDateString('fr-FR', {
                    day: 'numeric',
                    month: 'long',
                });
            };

            if (queryDate) {
                const start = parseDate(queryDate);
                const end = new Date(start);
                end.setDate(start.getDate() + 6);
                const past = new Date(start);
                const future = new Date(end);
                future.setDate(end.getDate() + 7);
                past.setDate(start.getDate() - 7);

                const tempDates = [];
                for (let d = new Date(start); d <= end; d.setDate(d.getDate() + 1)) {
                    tempDates.push(formatDate(d)); 
                }

                dates.value = tempDates;
                firstDate.value = formatDateB(start);
                lastDate.value = formatDateB(end); 

                firstDateNature.value = formatDate(past);
                lastDateNature.value = formatDate(future);
            } else {
                const currentWeekDates = getCurrentWeekDates(currentDate);
                dates.value = currentWeekDates.map(formatDate); 
                firstDate.value = formatDate(currentWeekDates[0]); 
                lastDate.value = formatDate(currentWeekDates[6]);
                firstDateNature.value = formatDate(currentWeekDates[0]); // Date actuelle
                lastDateNature.value = formatDate(currentWeekDates[6]); // Date actuelle
            }
        };

        onMounted(() => {
            initializeDates();
        });

        return { dates, firstDate, lastDate, firstDateNature, lastDateNature }; // Ajout de firstDateNature et lastDateNature ici
    },
});
</script>
  
  <style scoped>
  .parent-header-title {
    display: flex;
    justify-content: space-between;
    align-items: center
  }
  .title-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: auto;
  text-align: center;
  text-transform: uppercase;
}
  .line-titlecontent {
  width: 40%;
  height: 1px;
  background-color: #191919;
}
  .title-page {
  margin: 2% 0 2% 0;
  font-size: x-large; 
  text-transform: uppercase; 
  width: 100%; 
  text-align: center;
}
.parent-calendar {
    display: flex; 
    justify-content: space-around;
    list-style-type: none
}
.hours {
    display: grid;
}
.hours div {
    width: 100%;
}
li {
    width: 100%;
}
.hours .content-hour {
    min-height: 10vh;
    display: flex;
    align-items: center;
    background-color: rgb(190, 190, 190);
    border-right: 1px solid black;
    border-bottom: 1px solid black;
    text-transform: uppercase;
    width: 100%;

}
.hours .content-hour:nth-child(even) {
    background-color: rgb(205, 205, 205);
}
.hours .content-hour p {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 3%;
}
.date {
    text-align: center;
    border: 1px solid black;
    margin: 0;
    padding: 10px;
}
.hour-left {
    display: flex;
    justify-content: center;
    text-align: center;
    align-items: center;
    text-transform: uppercase;
    font-size: large;
    background-color: #bcbcbc;
    border: 1px solid black;
    min-height: 10vh;
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