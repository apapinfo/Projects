<template>
    <div class="MenuDeroulant">
        <div class="dropdown">
            <div class="dropdown-item">
                <router-link :to="{ name: 'Accueil' }" class="menu-link">
                    <p>Page d'Accueil</p>
                </router-link>
            </div>
            <div class="dropdown-item">
                <p class="menu-link">Costumes</p>
                <div class="dropdown-content">
                    <router-link :to="{ name: 'RechercherCostumes' }" class="submenu-link">
                        <p>Rechercher des costumes</p>
                    </router-link>
                    <router-link :to="{ name: 'AjoutCostume' }" class="submenu-link">
                        <p>Ajouter un costume</p>
                    </router-link>
                </div>
            </div>
            <div class="dropdown-item">
                <p class="menu-link">Pièces</p>
                <div class="dropdown-content">
                    <router-link :to="{ name: 'RechercherPieces' }" class="submenu-link">
                        <p>Rechercher des pièces</p>
                    </router-link>
                    <router-link :to="{ name: 'AjoutPiece' }" class="submenu-link">
                        <p>Ajouter une pièce</p>
                    </router-link>
                </div>
            </div>
            <div class="dropdown-item">
                <p class="menu-link">Personnes</p>
                <div class="dropdown-content">
                    <router-link :to="{ name: 'RechercherPersonnes' }" class="submenu-link">
                        <p>Rechercher des personnes</p>
                    </router-link>
                    <router-link :to="{ name: 'AjoutPersonne' }" class="submenu-link">
                        <p>Ajouter une personne</p>
                    </router-link>
                </div>
            </div>
            <div class="dropdown-item">
                <p class="menu-link">Emprunts</p>
                <div class="dropdown-content">
                    <router-link :to="{ name: 'GestionEmprunt' }" class="submenu-link">
                        <p>Gérer les emprunts</p>
                    </router-link>
                    <router-link :to="{ name: 'NouvelEmprunt' }" class="submenu-link">
                        <p>Faire un nouvel emprunt</p>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>
  
<style>
.MenuDeroulant {
    width: 100%;
    background-color: #2a363b;
    align-items: center;
}

.dropdown {
    display: flex;
    justify-content: space-around;
    font-weight: bold;
    font-size: large;
}

.dropdown-item {
    width: 100%;
    position: relative;
    display: inline-block;
    text-align: center;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: #2a363b;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    z-index: 1;
    border-radius: 5px;
}

.dropdown-item:hover .dropdown-content {
    display: block;
}

.menu-link,
.submenu-link {
    text-decoration: none;
    color: white;
    transition: color 0.5s;
}

.menu-link:hover,
.submenu-link:hover {
    color: red;
}
</style>
