<template>
  <div class="login">
    <h1>Connexion</h1>
    <form class="form">
      <div class="input">
        <label for="id">Identifiant</label><br />
        <input
          type="text"
          id="id"
          name="id"
          v-model="input.id"
          placeholder="Identifiant"
          required
        />
      </div>
      <div class="input">
        <label for="pwd">Mot de Passe</label><br>
        <input type="password" id="pwd" name="pwd" v-model="input.pwd" placeholder="Mot de passe" required/>

      </div>
      <button type="button" v-on:click="login(input.id, input.pwd)">Connexion</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Login',
  data() {
    return {
      input: {
        id: '',
        pwd: ''
      }
    }
  },

  methods: {
    async login(id, pwd) {
      try {
        const { data } = await axios
        .post("http://localhost:3000/utilisateurs/connexion", {
          identifiant: id,
          mdp: pwd
        });

        if (data)
          if (data.connexion == true)
            this.$router.push('/accueil');
        else
          console.log("identifiant ou mot de passe incorrect");

        return data;
      } catch (error) {
        console.log(error);
      }
    }
  }
}
</script>

<style>
.login {
  display: grid;
  place-items: center;
}

.form {
  width: 275px;
  height: 300px;
  margin: auto;
  background-color: #2a363b;
  color: #f8f8f8;
  border-radius: 5%;
}

.form .input {
  display: table;
  margin: 0 auto;
  padding: 20px;
  
}

.form input {
  height: 35px;
  font-size: 1.2em;
}

.form button {
  display: table;
  margin: 0 auto;
  margin-top: 20px;
  width: 200px;
  background-color: #f5d061;
  color: #000000;
  padding: 10px;
}

.form label {
  font-size: 24px;
}


</style>
