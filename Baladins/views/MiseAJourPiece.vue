<template>
    <MenuDeroulant />
    <div>
        <h1> Mettre A Jour Pièce </h1>
        <form class="formulaire-piece">
            <label for="IdLabel">
                <p> ID Piece </p>
            </label>
            <br>
            <input type="text" id="IdInput" v-model="idPiece" placeholder="Entrez l'Id de la pièce à modifier" size="30"
                required disabled />
            <br>
            <label for="NomPieceLabel">
                <p>Nom Piece</p>
            </label>
            <br>
            <input type="text" id="NomPieceInput" v-model="nom" placeholder="Entrez Pour Modifier Nom Piece" size="30"
                required />
            <br>
            <label for="MotsClePieceLabel">
                <p>Mots Cle Piece</p>
            </label>
            <br>
            <input type="text" id="MotsClePieceInput" v-model="motsCle" placeholder="Entrez Pour Modifier Mots Cle Piece"
                size="30" required />
            <br>
            <label for="EpoquePiece">
                <p>Epoque Piece</p>
            </label>
            <br>
            <select v-model="epoque">
                <option>Moyen-Age</option>
                <option>Renaissance</option>
                <option>Baroque</option>
                <option>Rococo</option>
                <option>Neoclassicisme</option>
                <option>Empire</option>
                <option>Ere Victorienne</option>
                <option>Belle Epoque</option>
            </select>
            <br>
            <input type="text" id="EpoquePieceInput" v-model="epoque" placeholder="Selectionnez Pour Modifier Epoque Piece"
                size="30" required disabled />
            <br>
            <label for="TaillePieceLabel">
                <p>Taille Piece</p>
            </label>
            <br>
            <select v-model="taille">
                <option>S</option>
                <option>M</option>
                <option>L</option>
                <option>XL</option>
                <option>XXL</option>
            </select>
            <br>
            <input type="text" id="TaillePieceInput" v-model="taille" placeholder="Entrez Pour Modifier Taille Piece"
                size="30" required disabled />
            <br>
            <label for="EtatPieceLabel">
                <p>Etat Piece</p>
            </label>
            <br>
            <select v-model="etat">
                <option>Neuf</option>
                <option>Bon</option>
                <option>Usé</option>
            </select>
            <br>
            <input type="text" id="EtatPieceInput" v-model="etat" placeholder="Entrez Pour Modifier Etat Piece" size="30"
                required disabled class="inputpiece" />
            <br>
            <label for="IdCostumePieceLabel">
                <p>ID du Costume concerné</p>
            </label>
            <br>
            <input type="text" id="IdCostumePieceInput" v-model="idCostume"
                placeholder="Entrez Pour Modifier Id Costume Piece" size="30" required />
            <br>
            <button type="button" v-on:click="MiseAJourPiece()"> Mettre A Jour Pièce </button>
            <br>
            <p v-if="pieceAJour">Pièce mise à jour avec succès !</p>
            <br>
            <p v-if="pieceAJour"> Vous allez être redirigé dans 5 secondes... </p>
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
            motsCle: this.$route.params.motsCle,
            epoque: this.$route.params.epoque,
            taille: this.$route.params.taille,
            etat: this.$route.params.etat,
            idCostume: this.$route.params.idCostume,
            idPiece: this.$route.params.idPiece,
            pieceAJour: false
        };
    },
    methods: {
        MiseAJourPiece() {
            const pieceData = {
                nom: this.nom,
                motsCle: this.motsCle,
                epoque: this.epoque,
                taille: this.taille,
                etat: this.etat,
                idCostume: this.idCostume
            };
            const idPiece = this.idPiece;
            if (this.idPiece && (this.nom || this.motsCle || this.epoque || this.taille || this.etat || this.idCostume)) {
                axios.put(`http://localhost:3000/pieces/update/${idPiece}`, pieceData)
                    .then(response => {
                        console.log("Pièce mise à jour : ", response.data);
                        // Réinitialisation du formulaire après la mise à jour
                        this.nom = '';
                        this.motsCle = '';
                        this.epoque = '';
                        this.taille = '';
                        this.etat = '';
                        this.idCostume = '';
                        this.idPiece = '';
                        this.pieceAJour = true;
                    },
                    setTimeout(() => {
                        this.$router.push({ name: 'RechercherPieces'})
                    }, 5000)

                    ).catch(error => {
                        console.error("Erreur lors de la mise à jour : ", error);
                    });
            } else {
                this.pieceAJour = false;
            }
        }
    }
};
</script>
  
<style>
.formulaire-piece {
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

.formulaire-piece p {
    font-size: auto;
    margin-bottom: 0px;
}

.formulaire-piece input {
  height: 35px;
  font-size: 1.2em;
}

.formulaire-piece button {
    margin-top: 20px;
    margin-bottom: 20px;
    width: 300px;
    background-color: #f5d061;
    color: #000000;
    padding: 10px;
}

.formulaire-piece select {
    width: 50%;
    margin-bottom: 20px;
}
</style>
  