<template>
  <div class="Notification">
    <img src="@/img/warning.png">
    <div class="contenuNotification">
      <h1 class="texteNotification"> Retard de costume </h1>
      <p class="texteNotification"> {{ emprunt.nom_personne }} {{ emprunt.prenom_personne }} n'a pas rendu son costume: {{ emprunt.emprunt_details.titre_costume }} </p>
      <h3 @click="AccederEmprunts()" class="texteNotification"> Accéder à la page de gestion des emprunts </h3>
    </div>
  </div>
</template>

<style>
.Notification {
  width: 80%; 
  height: 280px; 
  border-radius: 10%;
  background-color: rgb(255, 101, 101);
  margin: 30px auto;
}

.Notification img {
  width: 140px; 
  height: 140px;
  text-align: left;
  padding-left: 20px; 
  padding-top: 30px;
  display: inline-block;
  position: absolute;
}

.contenuNotification h1{
  font-size: 54px;
}

.contenuNotification p {
  text-align: center;
  font-size: 34px;
}

.contenuNotification h3 {
  text-align: center;
  border: 1px solid black;
  background-color: #f5d061;
  font-size: 34px;
}

.contenuNotification button {
  margin: auto; 
  background-color: red;
  align-items: center;
  justify-content: center;
}

.contenuNotification {
  margin: auto;
  padding-top: 5px;
}

.texteNotification {
  opacity: 100%;
  color: black;
}

</style>

<script>
export default {
  props:["emprunt"], 
  methods: {
  AccederEmprunts() {
    this.$router.push({name: "GestionEmprunt"});
  }
}
}

</script>