<template>
  <MenuDeroulant />
  <div>
    <h1> Ajouter Costume </h1>
    <form class="formulaire-costume">
      <label for="TitreLabel">
        <p> Titre Costume </p>
      </label>
      <br>
      <input type="text" id="TitreInput" v-model="titre" placeholder="Entrez Titre" size="20" required />
      <br>
      <label for="DescriptionLabel">
        <p> Description Costume </p>
      </label> <br>
      <textarea id="DescriptionTextArea" v-model="description" rows="8" cols="40" maxlength="256"
        placeholder="Entrez description" />
      <br>
      <small> Limite : 256 caractères </small> <br>
      <button type="button" v-on:click="AjouterCostume()"> Ajouter Costume </button>
      <br>
      <p v-if="costumeAjoute">Costume ajouté avec succès !</p>
      <br>
    </form>
  </div>
</template>

<script>
import MenuDeroulant from "@/components/MenuDeroulant.vue";
import axios from 'axios';

export default {
  components: {
    MenuDeroulant
  },
  data() {
    return {
      titre: '',
      description: '',
      costumeAjoute: false
    };
  },
  methods: {
    AjouterCostume() {
      const costumeData = {
        titre: this.titre,
        description: this.description
      };
      if (this.titre || this.description) {
        axios.post('http://localhost:3000/costumes/create', costumeData)
          .then(response => {
            console.log("Costume ajouté avec succès : ", response.data);
            // Réinitialisation du formulaire après l'ajout
            this.titre = '';
            this.description = '';
            this.costumeAjoute = true;
          })
          .catch(error => {
            console.error("Erreur lors de l'ajout du costume : ", error);
          });
      } else {
        this.costumeAjoute = false;
      }
    }
  }
};
</script>

<style>
.formulaire-costume {
  text-align: center;
  border-radius: 5px;
  padding-top: 50px;
  padding-bottom: 20px;
  width: 400px;
  height: auto;
  background-color: #2a363b;
  margin: auto;
  color: #ffffff;
}

.formulaire-costume p {
  font-size: auto;
  margin-bottom: 0px;
}

.formulaire-costume input {
  height: 35px;
  font-size: 1.2em;
}

.formulaire-costume button {
  margin-top: 20px;
  margin-bottom: 20px;
  width: 300px;
  background-color: #f5d061;
  color: #000000;
  padding: 10px;
}

.formulaire-costume small {
  font-size: 1.2em;
}

.formulaire-costume small {
  color: gray;
}

.formulaire-costume textarea {
  resize: none;
}
</style>
