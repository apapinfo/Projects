<template>
    <MenuDeroulant />
    <div>
        <h1> Mettre A Jour Personne </h1>
        <form class="formulaire-personne">
            <label for="IdLabel">
                <p> ID Personne </p>
            </label>
            <br>
            <input type="text" id="IdInput" v-model="idPersonne" placeholder="Entrez l'ID de la personne à modifier"
                size="30" required disabled />
            <br>
            <label for="NomLabel">
                <p> Modifier Nom </p>
            </label>
            <br>
            <input type="text" id="NomInput" v-model="nom" placeholder="Entrez Pour Modifier Nom" size="30" required />
            <br>
            <label for="PrenomLabel">
                <p> Prénom </p>
            </label>
            <br>
            <input type="text" id="PrenomInput" v-model="prenom" placeholder="Entrez Entrez Pour Modifier Prénom" size="30"
                required />
            <br>
            <label for="TelephoneLabel">
                <p> Numéro de téléphone </p>
            </label>
            <br>
            <input type="tel" id="TelephoneInput" v-model="telephone" pattern="[0-9]{10}"
                placeholder="Entrez Pour Modifier Numéro Téléphone" size="30" required />
            <br>
            <small>Format: 0123456789</small>
            <br>
            <label for="EmailLabel">
                <p> Email </p>
            </label>
            <br>
            <input type="email" id="EmailInput" v-model="email" size="30" placeholder="Entrez Pour Modifier Mail"
                required />
            <br>
            <small>Format: nomprenom@gmail.com</small>
            <br>
            <button type="button" v-on:click="MiseAJourPersonne()"> Mettre A Jour Personne </button>
            <br>
            <p v-if="personneAJour">Personne mise à jour avec succès !</p>
            <br>
            <p v-if="personneAJour">Vous allez être redirigé dans 5 secondes...</p>
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
            nom: this.$route.params.nom,
            prenom: this.$route.params.prenom,
            telephone: this.$route.params.telephone,
            email: this.$route.params.email,
            idPersonne: this.$route.params.idPersonne,
            personneAJour: false
        };
    },
    methods: {
        MiseAJourPersonne() {
            const personneData = {
                nom: this.nom,
                prenom: this.prenom,
                telephone: this.telephone,
                email: this.email
            };
            const idPersonne = this.idPersonne;
            if (this.idPersonne && (this.nom || this.prenom || this.telephone || this.email)) {
                axios.put(`http://localhost:3000/personnes/update/${idPersonne}`, personneData)
                    .then(response => {
                        console.log("Mise à jour réussie : ", response.data);
                        // Réinitialisation du formulaire après la mise à jour
                        this.nom = '';
                        this.prenom = '';
                        this.telephone = '';
                        this.email = '';
                        this.idPersonne = '';
                        this.personneAJour = true;
                    },
                    setTimeout(() => {
                        this.$router.push({ name: 'RechercherPersonnes'})
                    }, 5000)
                    ).catch(error => {
                        console.error("Erreur lors de la mise à jour : ", error);
                    });
            } else {
                this.personneAJour = false;
            }
        }
    }
};
</script> 

<style>
.formulaire-personne {
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

.formulaire-personne p {
    font-size: auto;
    margin-bottom: 0px;
}

.formulaire-personne input {
  height: 35px;
  font-size: 1.2em;
}

.formulaire-personne button {
    margin-top: 20px;
    margin-bottom: 20px;
    width: 300px;
    background-color: #f5d061;
    color: #000000;
    padding: 10px;
}

.formulaire-personne small {
    color: gray;
}

.formulaire-personne textarea {
    resize: none;
}
</style>
