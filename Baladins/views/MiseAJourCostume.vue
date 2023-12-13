<template>
    <MenuDeroulant />
    <div>
        <h1> Mettre A Jour Costume </h1>
        <form class="formulaire-costume">
            <label for="IdLabel">
                <p> ID Costume </p>
            </label>
            <br>
            <input type="text" id="IdInput" v-model="idCostume" placeholder="Entrez l'Id du costume à modifier" size="30"
                required disabled />
            <br>
            <label for="TitreLabel">
                <p> Titre Costume </p>
            </label>
            <br>
            <input type="text" id="TitreInput" v-model="titre" placeholder="Entrez Pour Modifier Titre" size="30"
                required />
            <br>
            <label for="DescriptionLabel">
                <p> Description Costume </p>
            </label> <br>
            <textarea id="DescriptionTextArea" v-model="description" rows="8" cols="40" maxlength="256"
                placeholder="Entrez Pour Modifier Description" />
            <br>
            <small> Limite : 256 caractères </small> <br>
            <button type="button" v-on:click="MiseAJourCostume()"> Mettre A Jour Costume </button>
            <br>
            <p v-if="costumeAJour">Costume mis à jour avec succès ! </p>
            <br>
            <p v-if="costumeAJour"> Vous allez être redirigé dans 5 secondes... </p>
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
            titre: this.$route.params.titre,
            description: this.$route.params.description,
            idCostume: this.$route.params.idCostume,
            costumeAJour: false
        };
    },
    methods: {
        MiseAJourCostume() {
            const costumeData = {
                titre: this.titre,
                description: this.description
            };
            const idCostume = this.idCostume;
            if (this.idCostume && (this.titre || this.description)) {
                axios.put(`http://localhost:3000/costumes/update/${idCostume}`, costumeData)
                    .then(response => {
                        console.log("Mise à jour réussie : ", response.data);
                        // Réinitialisation du formulaire après la mise à jour
                        this.titre = '';
                        this.description = '';
                        this.idCostume = '';
                        this.costumeAJour = true;
                    },
                    setTimeout(() => {
                        this.$router.push({ name: 'RechercherCostumes'})
                    }, 5000)
                    ).catch(error => {
                        console.error("Erreur lors de la mise à jour : ", error);
                    });
            } else {
                this.costumeAJour = false;
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
    padding-bottom: 50px;
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
    color: gray;
}

.formulaire-costume textarea {
    resize: none;
}
</style>
  