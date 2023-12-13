<template>
    <MenuDeroulant />
    <h1> Rechercher Pièces </h1>
    <div class="ListePieces">
        <div class="recherche">
            <br>
            <div>
                <input v-model="recherche" placeholder="Rechercher par nom, mot-clé, époque ou état" />
                <br>
                <small> Entrer '*' pour afficher toutes les pièces </small> <br>
                <br>
                <button @click="rechercherPieces()">Cliquer pour rechercher la pièce</button>
            </div>
            <div v-if="rechercheTerminee && piecesFiltrees.length == 0">
                <br>
                <p>Aucune pièce trouvée.</p>
                <br>
            </div>
        </div>
    </div>
    <div v-if="piecesFiltrees.length > 0">
        <br>
        <table border="1" class="tableau_emprunts">
            <tr>
                <th>id</th>
                <th>Nom</th>
                <th>Mot-clé</th>
                <th>Époque</th>
                <th>Taille</th>
                <th>État</th>
                <th>id costume</th>
            </tr>

            <tr v-for="piece in piecesFiltrees">
                <td>{{ piece.id_piece }}</td>
                <td>{{ piece.nom_piece }}</td>
                <td>{{ piece.motscle_piece }}</td>
                <td>{{ piece.epoque_piece }}</td>
                <td>{{ piece.taille_piece }}</td>
                <td>{{ piece.etat_piece }}</td>
                <td>{{ piece.id_costume }}</td>
                <td>
                    <button @click="modifierPiece(piece.id_piece, piece.nom_piece, piece.motscle_piece, piece.epoque_piece, piece.taille_piece, piece.etat_piece, piece.id_costume)" style="width:100%; font-size: 20px">Modifier</button>
                </td>
                <td>
                    <button @click="openPopUp(piece.id_piece, piece.nom_piece)" style="width:100%; font-size: 20px">Supprimer</button>
                </td>
            </tr>
        </table>
    </div>
    
    <div id="overlay"  @click="closePopUp()"> </div>

    <div id="popup_confirmation_suppression">
        <h1> Êtes vous surs de vouloir supprimer cette pièce: </h1>
        <h1> {{ titrePiecePopUp }} </h1>
        <h2> Cette action est irréversible. </h2>
        <button @click="supprimerPiece()"  class="bouton-oui-popup"> Oui </button>
        <button @click="closePopUp()"  class="bouton-non-popup"> Non </button>
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
            pieces: [],
            piecesFiltrees: [],
            rechercheTerminee: false,
            idPiecePopUp: 0, 
            titrePiecePopUp: ""
        };
    },
    methods: {
        modifierPiece(idPiece, nom, motsCle, epoque, taille, etat, idCostume) {
            this.$router.push({ name: 'MiseAJourPiece', params: { idPiece, nom, motsCle, epoque, taille, etat, idCostume} });
        },
        openPopUp(idPiece, titre){
            this.idPiecePopUp = idPiece;
            this.titrePiecePopUp = titre;
            document.getElementById('popup_confirmation_suppression').style.display = 'block';
            document.getElementById('overlay').style.display = 'block';
        },
        closePopUp() {
            document.getElementById('popup_confirmation_suppression').style.display = 'none';
            document.getElementById('overlay').style.display = 'none';
        },


        supprimerPiece() {
            const idPiecePopUp = this.idPiecePopUp;
            if (idPiecePopUp) {
                axios.delete(`http://localhost:3000/pieces/delete/${idPiecePopUp}`)
                    .then(response => {
                        console.log("Suppression réussie : ", response.data);
                        // Réinitialisation du formulaire après la suppression
                        this.idPiecePopUp = 0;
                        this.titrePiecePopUp = "";
                        location.reload();
                    })
                    .catch(error => {
                        console.error("Erreur lors de la suppression : ", error);
                    });
            } 
        }, 
        rechercherPieces() {
            // Réinitialiser l'état de recherche
            this.rechercheTerminee = false;
            this.piecesFiltrees = [];

            // Vérifier si la recherche est '*'
            if (this.recherche === '*') {
                // Afficher toutes les pièces
                this.piecesFiltrees = this.pieces;
            } else {
                // Filtrer les pièces en fonction de la recherche
                if (this.recherche) {
                    const rechercheMinuscules = this.recherche.toLowerCase();
                    this.piecesFiltrees = this.pieces.filter((piece) => {
                        return (
                            piece.nom_piece.toLowerCase().includes(rechercheMinuscules) ||
                            piece.motscle_piece.toLowerCase().includes(rechercheMinuscules) ||
                            piece.epoque_piece.toString().includes(this.recherche) ||
                            piece.etat_piece.toLowerCase().includes(rechercheMinuscules)
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
        axios.get('http://localhost:3000/pieces/findall').then((response) => {
            this.pieces = response.data;
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
</style>
  