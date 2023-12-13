<template>
  <MenuDeroulant />
  
  <h1 class="Bienvenue"> Bienvenue ! </h1>
  <div v-if=emprunts>
    <h1> Il y a {{ emprunts.length }} réservations en retard ! </h1>

    <div v-for="emprunt in emprunts">


      <Notification :emprunt="emprunt"> </Notification>
    </div>
    <h2> Aucune autre réservation en retard. </h2>
    
  </div>
  <div v-else>
    <h2> Aucune réservation en retard ! </h2>
  </div>
</template>

<script>
import MenuDeroulant from "@/components/MenuDeroulant.vue";
import Notification from "@/components/Notification.vue";
import axios from 'axios';

export default {
  components: {
    MenuDeroulant,
    Notification
  },
  data() {
    return {
      emprunts: {},
    }
  },

  methods: {
    async getLateReservations() {
      try {
        const {data} = await axios.get("http://localhost:3000/emprunts/late"); 
        this.emprunts = data; 
      } catch (error) {
        console.log(error);
      }
    },
    
  }, 
  beforeMount() {
    this.getLateReservations();
  }
}



</script>

<style>
h1,
h2 {
  text-align: center;
}

h1 {
  font-size: 3em;
}

h2 {
  font-size: 2em;
}

p {
  font-size: 2em;
}

</style>