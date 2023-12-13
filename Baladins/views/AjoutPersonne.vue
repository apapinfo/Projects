<template>
    <MenuDeroulant />
    <div>
        <h1> Ajouter Personne </h1>
        <form class="formulaire-personne">
            <label for="NomLabel">
                <p> Nom </p>
            </label>
            <br>
            <input type="text" id="NomInput" v-model="nom" placeholder="Entrez Nom" size="30" required />
            <br>
            <label for="PrenomLabel">
                <p> Prénom </p>
            </label>
            <br>
            <input type="text" id="PrenomInput" v-model="prenom" placeholder="Entrez Prénom" size="30" required />
            <br>
            <label for="TelephoneLabel">
                <p> Numéro de téléphone </p>
            </label>
            <br>
            <input type="tel" id="TelephoneInput" v-model="telephone" pattern="[0-9]{10}"
                placeholder="Entrez Numéro Téléphone" size="30" required />
            <br>
            <small>Format: 0123456789</small>
            <br>
            <label for="EmailLabel">
                <p> Email </p>
            </label>
            <br>
            <input type="email" id="EmailInput" v-model="email" size="30" placeholder="Entrez Mail" required />
            <br>
            <small>Format: nomprenom@gmail.com</small>
            <br>
            <button type="button" v-on:click="AjouterPersonne()"> Ajouter Personne </button>
            <br>
            <p v-if="personneAjoutee">Personne ajoutée avec succès !</p>
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
            nom: '',
            prenom: '',
            telephone: '',
            email: '',
            idPersonne: '',
            personnes: [],
            personneAjoutee: false
        };
    },
    methods: {
        AjouterPersonne() {
            const personneData = {
                nom: this.nom,
                prenom: this.prenom,
                telephone: this.telephone,
                email: this.email
            };
            if (this.nom || this.orenom || this.telephone || this.email) {
                axios.post('http://localhost:3000/personnes/create', personneData)
                    .then(response => {
                        console.log("Personne ajoutée avec succès : ", response.data);
                        // Réinitialisation du formulaire après l'ajout
                        this.nom = '';
                        this.prenom = '';
                        this.telephone = '';
                        this.email = '';
                        this.personneAjoutee = true;
                    })
                    .catch(error => {
                        console.error("Erreur lors de l'ajout de la personne : ", error);
                    });
            } else {
                this.personneAjoutee = false;
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
