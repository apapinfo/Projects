<template>
  <MenuDeroulant />
  <div>
    <h1> Gestion emprunts </h1>
    <h2> Costumes empruntés: </h2>
    <table border="1" class="tableau_emprunts">
      <tr>
        <th>Prénom Nom</th>
        <th>Costume Emprunté</th>
        <th>Date de début</th>
        <th>Date de fin</th>
      </tr>

      <tr v-for="emprunt in emprunts">
        <td>{{ emprunt.prenom_personne }} {{ emprunt.nom_personne }}</td>
        <td>
          <div v-for="costume in emprunt.info_costumes">
            ({{ costume.costume_id }}) {{ costume.costume_titre }}
          </div>
        </td>
        <td>{{ formatDate(emprunt.date_debut) }}</td>
        <td>{{ formatDate(emprunt.date_fin) }}</td>
        <td>
          <button @click="modifierEmprunt(emprunt.id_emprunt)" style="width:100%; font-size: 20px">Modifier</button>
        </td>
        <td>
          <button @click="openPopUp(emprunt.id_emprunt)" style="width:100%; font-size: 20px">Supprimer</button>
        </td>
      </tr>

    </table>

  </div>

  <div id="overlay"  @click="closePopUp()"> </div>

    <div id="popup_confirmation_suppression">
        <h1> Êtes vous surs de vouloir supprimer cet emprunt ? </h1>
        <h2> Cette action est irréversible. </h2>
        <button @click="supprimerEmprunt()"  class="bouton-oui-popup"> Oui </button>
        <button @click="closePopUp()"  class="bouton-non-popup"> Non </button>
    </div>

</template>

<script>
import MenuDeroulant from "@/components/MenuDeroulant.vue";
import axios from 'axios';

export default {
  name: "GestionEmprunt",
  data() {
    return {
      emprunts: {},
      idEmpruntPopUp: 0
    };
  },

  components: {
    MenuDeroulant
  },

  methods: {
    modifierEmprunt(id_emprunt) {
      this.$router.push({ name: 'ModifierEmprunt', params: { id_emprunt } });
    },
    openPopUp(idEmprunt){
      this.idEmpruntPopUp = idEmprunt;
      document.getElementById('popup_confirmation_suppression').style.display = 'block';
      document.getElementById('overlay').style.display = 'block';
    },
    closePopUp() {
      document.getElementById('popup_confirmation_suppression').style.display = 'none';
      document.getElementById('overlay').style.display = 'none';
    },
    supprimerEmprunt() {
      const idEmpruntPopUp = this.idEmpruntPopUp
            if (idEmpruntPopUp) {
                axios.delete('http://localhost:3000/emprunts/delete/' + idEmpruntPopUp)
                .then(response => {
                    console.log("Suppression réussie : ", response.data);
                    this.idEmpruntPopUp = 0; 
                    location.reload();
                })
                .catch(error => {
                    console.error("Erreur lors de la suppression : ", error);
                });
            } 
        },
    async getAllBorrowing() {
      try {
        const { data } = await axios.get("http://localhost:3000/emprunts/findall");
        this.emprunts = data;
      } catch (error) {
        console.log(error);
      }
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toISOString().split('T')[0];
    }
  },
  beforeMount() {
    this.getAllBorrowing();
  },
}
</script>

<style>
.tableau_emprunts {
  text-align: center;
  border-radius: 5px;
  margin: auto;
  background-color: #2a363b;
  color: white;
  width: 1500px;
}

.tableau_emprunts th {
  width: auto;
  height: 30px;
  font-size: 3em;
}

.tableau_emprunts td {
  width: auto;
  font-size: 2em;
}
</style>