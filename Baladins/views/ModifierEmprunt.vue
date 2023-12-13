<template>
    <MenuDeroulant />
    <div>
        <h1>Modifier Emprunt</h1>
        <form class="formulaire-emprunt">
            <div>
                <label for="id_emprunt">id Emprunt :</label>
            </div>
            <br>
            <div>
                <input type="text" id="id_emprunt" name="id_emprunt" v-model="input.id_emprunt" placeholder="x" required disabled />
            </div>
            <br>
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
                <input type="text" id="id_costume" name="id_costume" v-model="input.id_costume" placeholder="Costume"
                    required />
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
                    v-on:click="modifierEmprunt(input.id_emprunt, input.date_debut, input.date_fin, input.id_personne, input.id_costume)">Modifier
                    l'emprunt</button>
            </div>
            <br>
            <p v-if="empruntMisAJour">Emprunt mis à jour avec succès ! </p>
            <br>
            <p v-if="empruntMisAJour"> Vous allez être redirigé dans 5 secondes... </p>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

import MenuDeroulant from "@/components/MenuDeroulant.vue";
import SearchBar from "@/components/SearchBar.vue";

export default {
    name: "ModifierEmprunt",
    data() {
        return {
            input: {
                id_emprunt: this.$route.params.id_emprunt,
                date_debut: '',
                date_fin: '',
                id_personne: '',
                id_costume: ''
            },
            empruntMisAJour: false 
        };
        
    },

    components: {
        MenuDeroulant,
        SearchBar
    },

    methods: {
        async modifierEmprunt(id_emprunt, debut_date, fin_date, personne_id, costume_id) {
            try {
                const { data } = await axios
                    .put('http://localhost:3000/emprunts/update/' + id_emprunt, {
                        date_debut: debut_date,
                        date_fin: fin_date,
                        id_personne: personne_id,
                        id_costume: costume_id
                    });

                this.status = data;
                this.empruntMisAJour = true 

                setTimeout(() => {
                        this.$router.push({ name: 'GestionEmprunt'})
                    }, 5000)
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

.formulaire-emprunt p {
    font-size: auto;
    margin-bottom: 0px;
}

.formulaire-emprunt input {
  height: 35px;
  font-size: 1.2em;
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
