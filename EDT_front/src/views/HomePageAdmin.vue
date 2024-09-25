<template>
    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-title><a href="/home">Home Page Admin</a></ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content>
            <ion-button @click="openCardAllGroups">Les groupes</ion-button>
            <ion-button @click="openCardCreate">Créer un groupe</ion-button>
            <ion-card v-if="showCard">
                <ion-card-header>
                    <ion-card-title>Créer un nouveau groupe</ion-card-title>
                </ion-card-header>
                <ion-card-content>
                    <ion-item>
                        <ion-label position="floating">Nom du groupe</ion-label>
                        <ion-input v-model="groupName"></ion-input>
                    </ion-item>
                    <ion-item>
                        <ion-label position="floating">Ajouter des utilisateurs</ion-label>
                        <div class="tags-input">
                            <div v-for="(user, index) in users" :key="index" class="tag">
                                {{ user }}
                                <ion-icon name="close-circle" @click="removeUser(index)"></ion-icon>
                            </div>
                            <ion-input v-model="newUser" @keyup.enter="addUser"></ion-input>
                        </div>
                    </ion-item>
                    <ion-button expand="full" @click="createGroup">Créer</ion-button>
                </ion-card-content>
            </ion-card>
        </ion-content>
    </ion-page>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonButton, IonCard, IonCardHeader, IonCardTitle, IonCardContent, IonItem, IonLabel, IonInput, IonIcon } from '@ionic/vue';

export default defineComponent({
    name: 'HomePageAdmin',
    components: {
        IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonButton, IonCard, IonCardHeader, IonCardTitle, IonCardContent, IonItem, IonLabel, IonInput, IonIcon
    },
    setup() {
        const showCard = ref(false);
        const groupName = ref('');
        const users = ref<string[]>([]);
        const newUser = ref('');

        const openCardCreate = () => {
            showCard.value = !showCard.value;
        };

        const openCardAllGroups = () => {
        };

        const addUser = () => {
            if (newUser.value && !users.value.includes(newUser.value)) {
                users.value.push(newUser.value);
                newUser.value = '';
            }
        };

        const removeUser = (index: number) => {
            users.value.splice(index, 1);
        };

        const allGroupes = () => {
            // Logic to create group with groupName and users
            console.log('Group Name:', groupName.value);
            console.log('Users:', users.value);
        };

        const createGroup = () => {
            // Logic to create group with groupName and users
            console.log('Group Name:', groupName.value);
            console.log('Users:', users.value);
        };

        const profil = () => {
            // Logic to create group with groupName and users
            console.log('Group Name:', groupName.value);
            console.log('Users:', users.value);
        };

        return {
            showCard,
            groupName,
            users,
            newUser,
            openCardCreate,
            openCardAllGroups,
            addUser,
            removeUser,
            createGroup,
            allGroupes,
            profil
        };
    }
});
</script>

<style scoped>
.tags-input {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.tag {
    display: flex;
    align-items: center;
    background-color: #e0e0e0;
    padding: 4px 8px;
    border-radius: 4px;
}

.tag ion-icon {
    margin-left: 4px;
    cursor: pointer;
}
</style>