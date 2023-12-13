<template>
    <form class="formulaire-piece">
        <label for="nom-piece"> <p> Nom </p> </label> <br>
        <input type="text" id="nom-piece" name="nom-piece" placeholder="Nom de la piece" required /> <br>

        <label for="etat-piece"> <p> Etat </p> </label> <br>
        <input type="text" id="etat-piece" name="etat-piece" placeholder="Etat de la pièce" required /> <br>
    </form>
</template>

<style>
    .formulaire-piece {
        text-align: center;
        width: 300px; 
        height: 220px; 
        background-color: #2a363b;
        border-radius: 5%;
        margin: 0 auto;
    }

    .formulaire-piece p {
        font-size: 20px;
        padding-top: 10px;
        margin-bottom: 0px; 
    }
</style>