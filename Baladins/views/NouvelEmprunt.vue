<template>
  <MenuDeroulant />
  <div>
    <h1>Nouvel Emprunt</h1>
    <!--
    <div class=costume-nouvel-emprunt>
      <h2> Costume emprunté: pas encore validé </h2>
      <button> Rechercher </button>
    </div>
    <div class="personne-nouvel-emprunt">
      <h2> Personne: pas encore validée </h2>
      <SearchBar> </SearchBar>
    </div>
    <button> Valider la réservation </button>
    -->
    <form class="formulaire-emprunt">
      <div>
        <label for="id_personne">Personne :</label>
      </div>
      <br>
      <div>
        <input type="text" id="id_personne" name="id_personne" v-model="input.id_personne" placeholder="Personne"
          required />
      </div>
      <br>
      <div>
        <label for="id_costume">Costume :</label>
      </div>
      <br>
      <div>
        <input type="text" id="id_costume" name="id_costume" v-model="input.id_costume" placeholder="Costume" required />
      </div>
      <br>
      <div>
        <label for="date_debut">date de début emprunt :</label>
      </div>
      <br>
      <div>
        <input type="date" id="date_debut" name="date_debut" v-model="input.date_debut" required />
      </div>
      <br>
      <div>
        <label for="date_fin">date de fin emprunt :</label>
      </div>
      <br>
      <div>
        <input type="date" id="date_fin" name="date_fin" v-model="input.date_fin" required />
      </div>
      <br>
      <div>
        <button type="button"
          v-on:click="ajoutEmprunt(input.id_personne, input.date_debut, input.date_fin, input.id_costume)">Ajout
          d'emprunt</button>
      </div>
      <br>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

import MenuDeroulant from "@/components/MenuDeroulant.vue";
import SearchBar from "@/components/SearchBar.vue";

export default {
  name: "NouvelEmprunt",
  data() {
    return {
      input: {
        id_personne: '',
        id_costume: '',
        date_debut: '',
        date_fin: ''
      }
    };
  },

  components: {
    MenuDeroulant,
    SearchBar
  },

  methods: {
    async ajoutEmprunt(personne_id, debut_date, fin_date, costume_id) {
      try {
        const { data } = await axios
          .post("http://localhost:3000/emprunts/create", {
            id_personne: personne_id,
            date_debut: debut_date,
            date_fin: fin_date,
            id_costume: costume_id
          });

        this.status = data;
      } catch (error) {
        console.log(error);
      }
    }
  }
}
</script>

<style>
.formulaire-emprunt {
  text-align: center;
  border-radius: 5px;
  padding-top: 50px;
  padding-bottom: 50px;
  width: 400px;
  height: auto;
  background-color: #2a363b;
  margin: auto;
  color: #ffffff;
}

.formulaire-emprunt label {
  font-size: 2em;
}

.formulaire-emprunt button {
  margin-top: 20px;
  margin-bottom: 20px;
  width: 300px;
  background-color: #f5d061;
  color: #000000;
  padding: 10px;
}
</style>
