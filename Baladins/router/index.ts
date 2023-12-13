import { createRouter, createWebHistory } from 'vue-router'

import Login from '@/views/Login.vue'
import Accueil from '@/views/Accueil.vue'
import AjoutCostume from "@/views/AjoutCostume.vue"
import MiseAJourCostume from "@/views/MiseAJourCostume.vue"
import RechercherCostumes from "@/views/RechercherCostumes.vue"
import AjoutPiece from "@/views/AjoutPiece.vue"
import MiseAJourPiece from "@/views/MiseAJourPiece.vue"
import RechercherPieces from "@/views/RechercherPieces.vue"
import AjoutPersonne from "@/views/AjoutPersonne.vue"
import MiseAJourPersonne from "@/views/MiseAJourPersonne.vue"
import RechercherPersonnes from "@/views/RechercherPersonnes.vue"
import GestionEmprunt from "@/views/GestionEmprunt.vue"
import NouvelEmprunt from "@/views/NouvelEmprunt.vue"
import ModifierEmprunt from "@/views/ModifierEmprunt.vue"

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/accueil',
    name: 'Accueil',
    component: Accueil,
    meta: { requireAuth: true }
  },
  {
    path: '/ajout-costume',
    name: 'AjoutCostume',
    component: AjoutCostume,
    meta: { requireAuth: true }
  },
  {
    path: '/miseajour-costume/:idCostume/:titre/:description',
    name: 'MiseAJourCostume',
    component: MiseAJourCostume,
    meta: { requireAuth: true }
  },
  {
    path: '/rechercher-costumes',
    name: 'RechercherCostumes',
    component: RechercherCostumes,
    meta: { requireAuth: true }
  },
  {
    path: '/ajout-piece',
    name: 'AjoutPiece',
    component: AjoutPiece,
    meta: { requireAuth: true }
  },
  {
    path: '/miseajour-piece/:idPiece/:nom/:motsCle/:epoque/:taille/:etat/:idCostume',
    name: 'MiseAJourPiece',
    component: MiseAJourPiece,
    meta: { requireAuth: true }
  },
  {
    path: '/rechercher-pieces',
    name: 'RechercherPieces',
    component: RechercherPieces,
    meta: { requireAuth: true }
  },
  {
    path: "/ajout-personne",
    name: "AjoutPersonne",
    component: AjoutPersonne,
    meta: { requireAuth: true }
  }, 
  {
    path: "/miseajour-personne/:idPersonne/:nom/:prenom/:telephone/:email",
    name: "MiseAJourPersonne",
    component: MiseAJourPersonne,
    meta: { requireAuth: true }
  }, 
  {
    path: "/rechercher-personnes",
    name: "RechercherPersonnes",
    component: RechercherPersonnes,
    meta: { requireAuth: true }
  }, 
  {
    path: "/gestion-emprunt",
    name: "GestionEmprunt",
    component: GestionEmprunt,
    meta: { requireAuth: true }
  },
  {
    path: "/nouvel-emprunt",
    name: "NouvelEmprunt",
    component: NouvelEmprunt,
    meta: { requireAuth: true }
  }, 
  {
    path: "/modifier-emprunt/:id_emprunt",
    name: "ModifierEmprunt",
    component: ModifierEmprunt,
    meta: { requireAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
