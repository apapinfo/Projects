<template>
    <MenuDeroulant />
    <h1> Rechercher Costumes </h1>
    <div class="ListeCostumes">
        <div class="recherche">
            <br>
            <div>
                <input v-model="recherche" placeholder="Rechercher par titre ou description" />
                <br>
                <small> Entrer '*' pour afficher tous les costumes </small> <br>
                <br>
                <button @click="rechercherCostumes()">Cliquer pour rechercher le costume</button>
            </div>
            <div v-if="rechercheTerminee && costumesFiltres.length == 0">
                <br>
                <p> Aucun costume trouvé </p>
                <br>
            </div>
        </div>
    </div>
    <div v-if="costumesFiltres.length > 0">
        <br>
        <table border="1" class="tableau_emprunts">
            <tr>
                <th>id</th>
                <th>Titre</th>
                <th>Description</th>
            </tr>

            <tr v-for="costume in costumesFiltres">
                <td>{{ costume.id_costume }}</td>
                <td>{{ costume.titre_costume }}</td>
                <td>{{ costume.description_costume }}</td>
                <td>
                    <button @click="modifierCostume(costume.id_costume, costume.titre_costume, costume.description_costume)" style="width:100%; font-size: 20px">Modifier</button>
                </td>
                <td>
                    <button @click="openPopUp(costume.id_costume, costume.titre_costume)" style="width:100%; font-size: 20px">Supprimer</button>
                </td>
            </tr>

        </table>
    </div>
    
    <div id="overlay" @click="closePopUp()"> </div>

    <div id="popup_confirmation_suppression">
        <h1> Êtes vous surs de vouloir supprimer ce costume: </h1>
        <h1> {{ titreCostumePopUp }} </h1>
        <h2> Cette action est irréversible. </h2>
        <button @click="supprimerCostume()" class="bouton-oui-popup"> Oui </button>
        <button @click="closePopUp()" class="bouton-non-popup"> Non </button>
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
            costumes: [],
            costumesFiltres: [],
            rechercheTerminee: false,
            idCostumePopUp: 0, 
            titreCostumePopUp: ""
        };
    },
    methods: {
        modifierCostume(idCostume, titre, description) {
            this.$router.push({ name: 'MiseAJourCostume', params: { idCostume, titre, description} });
        },
        openPopUp(idCostume, titre){
            this.idCostumePopUp = idCostume;
            this.titreCostumePopUp = titre;
            document.getElementById('popup_confirmation_suppression').style.display = 'block';
            document.getElementById('overlay').style.display = 'block';
        },
        closePopUp() {
            document.getElementById('popup_confirmation_suppression').style.display = 'none';
            document.getElementById('overlay').style.display = 'none';
        },
        supprimerCostume() {
            const idCostumePopUp = this.idCostumePopUp
            if (idCostumePopUp) {
                axios.delete(`http://localhost:3000/costumes/delete/${idCostumePopUp}`)
                .then(response => {
                    console.log("Suppression réussie : ", response.data);
                    this.idCostumePopUp = 0; 
                    this.titreCostumePopUp = ""; 
                    location.reload();
                })
                .catch(error => {
                    console.error("Erreur lors de la suppression : ", error);
                });
            } 
            },
        
        rechercherCostumes() {
            // Réinitialiser l'état de recherche
            this.rechercheTerminee = false;
            this.costumesFiltres = [];

            // Vérifier si la recherche est '*'
            if (this.recherche === '*') {
                // Afficher toutes les pièces
                this.costumesFiltres = this.costumes;
            } else {
                // Filtrer les pièces en fonction de la recherche
                if (this.recherche) {
                    const rechercheMinuscules = this.recherche.toLowerCase();
                    this.costumesFiltres = this.costumes.filter((costume) => {
                        return (
                            costume.titre_costume.toLowerCase().includes(rechercheMinuscules) ||
                            costume.description_costume.toLowerCase().includes(rechercheMinuscules)
                        );
                    });
                }
            }

            // Mettre à jour l'indicateur de recherche terminée
            this.rechercheTerminee = true;
        },
    },
    created() {
        // Récupérer toutes les pièces au chargement du composant
        axios.get('http://localhost:3000/costumes/findall').then((response) => {
            this.costumes = response.data;
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
    width: 300px;
    padding: 10px;
}

td button {
    margin-top: 20px;
    margin-bottom: 20px;
    width: 80%;
    background-color: #f5d061;
    color: #000000;
    padding: 10px;
}

#popup_confirmation_suppression {
    display: none;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    z-index: 999;
    background-color: #f5d061;
    border-radius: 10%;
}

#overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    z-index: 998;
}

#popup_confirmation_suppression h1 {
    text-align: center; 
    font-size: 60px;
}

#popup_confirmation_suppression h2{
    font-size: 2em;
}

#popup_confirmation_suppression button{
    display: block;
    align-items: center;
    margin: 0 auto;
    width: 100px; 
    height: 80px; 
    font-size: 30px;
    margin-bottom: 40px;
}

.bouton-oui-popup{
    background-color: greenyellow;
} 

.bouton-non-popup{
    background-color: red;
} 

</style>
  
