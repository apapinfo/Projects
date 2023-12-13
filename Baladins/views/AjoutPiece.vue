<template>
    <MenuDeroulant />
    <div>
        <h1> Ajouter Pièce </h1>
        <form class="formulaire-piece">
            <label for="NomPieceLabel">
                <p>Nom Piece</p>
            </label>
            <br>
            <input type="text" id="NomPieceInput" v-model="nom" placeholder="Entrez Nom Piece" size="30" required />
            <br>
            <label for="MotsClePieceLabel">
                <p>Mots Cle Piece</p>
            </label>
            <br>
            <input type="text" id="MotsClePieceInput" v-model="motsCle" placeholder="Entrez Mots Cle Piece" size="30"
                required />
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
            <input type="text" id="EpoquePieceInput" v-model="epoque" placeholder="Selectionnez Epoque Piece" size="30"
                required disabled />
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
            <input type="text" id="TaillePieceInput" v-model="taille" placeholder="Entrez Taille Piece" size="30"
                required disabled />
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
            <input type="text" id="EtatPieceInput" v-model="etat" placeholder="Entrez Etat Piece" size="30" required disabled />
            <br>
            <label for="IdCostumePieceLabel">
                <p>ID du Costume concerné</p>
            </label>
            <br>
            <input type="text" id="IdCostumePieceInput" v-model="idCostume" placeholder="Entrez Id Costume Piece" size="30"
                required />
            <br>
            <button type="button" v-on:click="AjouterPiece()"> Ajouter Pièce </button>
            <br>
            <p v-if="pieceAjoutee">Pièce ajoutée avec succès !</p>
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
            motsCle: '',
            epoque: '',
            taille: '',
            etat: '',
            idCostume: '',
            pieceAjoutee: false,
            valeurChoisie: ''
        };
    },
    methods: {
        AjouterPiece() {
            const pieceData = {
                nom: this.nom,
                motsCle: this.motsCle,
                epoque: this.epoque,
                taille: this.taille,
                etat: this.etat,
                idCostume: this.idCostume
            };
            if (this.nom && this.motsCle && this.epoque && this.taille && this.etat && this.idCostume) {
                axios.post('http://localhost:3000/pieces/create', pieceData)
                    .then(response => {
                        console.log("Pièce ajoutée avec succès : ", response.data);
                        // Réinitialisation du formulaire après l'ajout
                        this.nom = '';
                        this.motsCle = '';
                        this.epoque = '';
                        this.taille = '';
                        this.etat = '';
                        this.idCostume = '';
                        this.pieceAjoutee = true;
                    })
                    .catch(error => {
                        console.error("Erreur lors de l'ajout de la pièce : ", error);
                    });
            } else {
                this.pieceAjoutee = false;
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
  