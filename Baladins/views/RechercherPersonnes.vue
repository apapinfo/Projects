<template>
    <MenuDeroulant />
    <h1> Rechercher Personnes </h1>
    <div class="ListePersonnes">
        <div class="recherche">
            <br>
            <div>
                <input v-model="recherche" placeholder="Rechercher par nom, prénom, email ou tel" />
                <br>
                <small> Entrer '*' pour afficher toutes les personnes </small> <br>
                <br>
                <button @click="rechercherPersonnes()">Cliquer pour rechercher la personne</button>
            </div>
            <div v-if="rechercheTerminee && personnesFiltrees.length == 0">
                <br>
                <p> Aucune personne trouvée </p>
                <br>
            </div>
        </div>
    </div>
    <br>
    <div v-if="personnesFiltrees.length > 0">

        <table border="1" class="tableau_emprunts">
            <tr>
                <th>id</th>
                <th>Prénom</th>
                <th>Nom</th>
                <th>Email</th>
                <th>Téléphone</th>
            </tr>

            <tr v-for="personne in personnesFiltrees">
                <td>{{ personne.id_personne }}</td>
                <td>{{ personne.prenom }}</td>
                <td>{{ personne.nom }}</td>
                <td>{{ personne.email }}</td>
                <td>{{ personne.telephone }}</td>
                <td>
                    <button @click="modifierPersonne(personne.id_personne, personne.nom, personne.prenom, personne.telephone, personne.email)" style="width:100%; font-size: 20px">Modifier</button>
                </td>
                <td>
                    <button @click="openPopUp(personne.id_personne, personne.nom, personne.prenom)" style="width:100%; font-size: 20px">Supprimer</button>
                </td>
            </tr>

        </table>

        <div id="overlay"  @click="closePopUp()"> </div>

        <div id="popup_confirmation_suppression">
            <h1> Êtes vous surs de vouloir supprimer cette personne: </h1>
            <h1> {{ nomPersonnePopUp }} {{ prenomPersonnePopUp }} </h1>
            <h2> Cette action est irréversible. </h2>
            <button @click="supprimerPersonne()"  class="bouton-oui-popup"> Oui </button>
            <button @click="closePopUp()"  class="bouton-non-popup"> Non </button>
        </div>

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
            recherche: '',
            personnes: [],
            personnesFiltrees: [],
            rechercheTerminee: false,
            idPersonnePopUp: 0, 
            nomPersonnePopUp: "", 
            prenomPersonnePopUp: ""
        };
    },
    methods: {
        modifierPersonne(idPersonne, nom, prenom, telephone, email) {
            // Rediriger vers la page de mise à jour avec l'id de la personne
            this.$router.push({ name: 'MiseAJourPersonne', params: { idPersonne, nom, prenom, telephone, email} });
        },
        openPopUp(idPersonne, nom, prenom){
            this.idPersonnePopUp = idPersonne;
            this.nomPersonnePopUp = nom;
            this.prenomPersonnePopUp = prenom; 
            document.getElementById('popup_confirmation_suppression').style.display = 'block';
            document.getElementById('overlay').style.display = 'block';
        },
        closePopUp() {
            document.getElementById('popup_confirmation_suppression').style.display = 'none';
            document.getElementById('overlay').style.display = 'none';
        },
        supprimerPersonne() {
            const idPersonnePopUp = this.idPersonnePopUp;
            if (idPersonnePopUp) {
                axios.delete(`http://localhost:3000/personnes/delete/${idPersonnePopUp}`)
                    .then(response => {
                        console.log("Suppression réussie : ", response.data);
                        // Réinitialisation du formulaire après la suppression
                        this.idPersonnePopUp = 0;
                        this.nomPersonnePopUp = ""; 
                        this.prenomPersonnePopUp = "";
                        location.reload();
                    })
                    .catch(error => {
                        console.error("Erreur lors de la suppression : ", error);
                    });
            } 
        },
        rechercherPersonnes() {
            // Réinitialiser l'état de recherche
            this.rechercheTerminee = false;
            this.personnesFiltrees = [];

            // Vérifier si la recherche est '*'
            if (this.recherche === '*') {
                // Afficher toutes les personnes
                this.personnesFiltrees = this.personnes;
            } else {
                // Filtrer les personnes en fonction de la recherche
                if (this.recherche) {
                    const rechercheMinuscules = this.recherche.toLowerCase();
                    this.personnesFiltrees = this.personnes.filter((personne) => {
                        return (
                            personne.nom.toLowerCase().includes(rechercheMinuscules) ||
                            personne.prenom.toLowerCase().includes(rechercheMinuscules) ||
                            personne.email.toLowerCase().includes(rechercheMinuscules) ||
                            personne.telephone.toLowerCase().includes(rechercheMinuscules)
                        );
                    });
                }
            }

            // Mettre à jour l'indicateur de recherche terminée
            this.rechercheTerminee = true;
        },
    },
    created() {
        // Récupérer toutes les personnes au chargement du composant
        axios.get('http://localhost:3000/personnes/findall').then((response) => {
            this.personnes = response.data;
        });
    },
};
</script>

<style>
.recherche {
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

.recherche p {
    font-size: auto;
}

.recherche button {
    margin-top: 20px;
    margin-bottom: 20px;
    width: 300px;
    background-color: #f5d061;
    color: #000000;
    padding: 10px;
}

.recherche small {
    color: gray;
}

.recherche input {
    margin-top: 20px;
    margin-bottom: 20px;
    width: 350px;
    padding: 10px;
    height: 35px;
    font-size: 1.2em;
}

.recherche small {
    font-size: 20px;
}

td button {
    margin-top: 20px;
    margin-bottom: 20px;
    width: 80%;
    background-color: #f5d061;
    color: #000000;
    padding: 10px;
}
</style>
