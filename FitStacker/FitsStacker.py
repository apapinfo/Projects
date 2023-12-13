# Pap Alexandre
# Pruvost Alban
# BUT2 TD1 TPA
# SAE C2
# Logiciel FitsStacker


# Importations des bibliothèques


# utilisation de os pour lister tous les noms de fichiers d'un dossier sous forme de chaines de caractères
import os
# utilisation de sys pour fermer la fenêtre et arrêter l'application
import sys
# utilisation des QtWidgets de PyQt6 pour créer et afficher la fenêtre, ses sous-fenêtres, ses éléments graphiques, ...
from PyQt6.QtWidgets import QMainWindow, QApplication, QListWidget, QScrollBar, QSlider, QComboBox, QLabel, QFileDialog, QPushButton, QMdiSubWindow
# utilisation de Qt de PyQt6 pour définir l'alignement des textes et l'orientation / personnalisation des QtWidgets
from PyQt6.QtCore import Qt
# utilisation de pyplot pour créer une figure contenant des images sous forme de tableaux numpy et pour afficher ces images dans un canevas
import matplotlib.pyplot as plt
# utilisation de FigureCanvasQtAgg pour créer un canevas dans une fenêtre pour afficher la figure contenant les images sous forme de tableaux numpy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# utilisation de get_pkg_data_filename pour récupérer une image FITS à partir des emplacements standards du paquet en retournant un nom de fichier local pour les données sous la forme d'un string
from astropy.utils.data import get_pkg_data_filename
# utilisation de fits pour la méthode getdata() pour lire les données d'une image FITS
from astropy.io import fits
# utilisation de numpy pour transformer les images FITS en tableau numpy ndarray pour pouvoir les afficher dans la fenêtre et les modifier
# Un ndarray est un conteneur multidimensionnel (généralement de taille fixe) d'éléments de même type et de même taille. Le nombre de dimensions et d'éléments d'un tableau est défini par sa forme, qui est un tuple de N entiers non négatifs spécifiant la taille de chaque dimension.
import numpy as np
# utilisation de Image de PIL pour sauvegarder une image FITS sous la forme d'un tableau numpy ndarray en image FITS
from PIL import Image


# Création de la classe Fenêtre


class Fenetre(QMainWindow):
    
	def __init__(self):
     
		super().__init__()
  
		# Création de la fenêtre
  
		self.setWindowTitle("FitsStacker")
		self.setFixedSize(1000, 600)
		self.setStyleSheet("background-color: rgb(61, 61, 61);")
  
		# Création du label canvas et zoom
  
		self.label_canvas_et_zoom = QLabel("  Canvas & Zoom", self)
		# Géométrie du QLabel
		self.label_canvas_et_zoom.setGeometry(0, 0, 630, 560)
		# Position du QLabel centrée dans la fenêtre
		self.label_canvas_et_zoom.move(int((self.frameGeometry().width() - self.label_canvas_et_zoom.width()) / 2), 25)
		# Modification de la couleur du fond, de la bordure, de la taille de police et de la couleur de police du QLabel
		self.label_canvas_et_zoom.setStyleSheet("background-color: rgb(61, 61, 61); border: 2px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")	
		# Alignement du texte du QLabel
		self.label_canvas_et_zoom.setAlignment(Qt.AlignmentFlag.AlignTop)
  
		# Création du label du chemin de fichier

		self.label_chemin_fichier = QLabel("Chemin du dossier affiché à chaque nouvel empilement", self)
		self.label_chemin_fichier.setGeometry(0, 0, 400, 25)
		self.label_chemin_fichier.move(int((self.frameGeometry().width() - self.label_chemin_fichier.width()) / 2), 10)
		self.label_chemin_fichier.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")		
		self.label_chemin_fichier.setAlignment(Qt.AlignmentFlag.AlignCenter)

		# Création de la figure et du canvas des images

		self.figure_images = plt.figure(figsize = (10, 7))
		# Le canevas contient la figure affichant les tableaux numpy ndarray
		self.canvas_images = FigureCanvas(self.figure_images)
  
		# Création de la sous-fenêtre contenant le canvas des images
  
		self.sous_fenetre_images = QMdiSubWindow(self)
		# La sous-fenêtre contient et affiche le canevas dans la fenêtre principale
		self.sous_fenetre_images.setWidget(self.canvas_images)
		self.sous_fenetre_images.setGeometry(0, 0, 590, 430)
		self.sous_fenetre_images.move(int((self.frameGeometry().width() - self.sous_fenetre_images.width()) / 2), 55)
		# Les bordures de la sous-fenêtre contenant et affichant le canevas sont cachées
		self.sous_fenetre_images.setWindowFlags(Qt.WindowType.FramelessWindowHint)
  
		# Création d'un bouton reset
  
		self.bouton_reset = QPushButton('Reset', self)
		self.bouton_reset.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		# Connexion du bouton Reset à la méthode reset() lorsqu'on clique sur le bouton
		self.bouton_reset.clicked.connect(self.reset)
		self.bouton_reset.move(int((self.frameGeometry().width() - self.bouton_reset.width()) / 2), 490)
  
		# Création d'un bouton floutage
  
		self.bouton_floutage = QPushButton('Floutage', self)
		self.bouton_floutage.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		# Connexion du bouton Floutage à la méthode floutage() lorsqu'on clique sur le bouton
		self.bouton_floutage.clicked.connect(self.flouter)
		self.bouton_floutage.move(int((self.frameGeometry().width() - self.bouton_reset.width()) / 2), 520)
  
		# Création d'un bouton inversion couleurs
  
		self.bouton_inversion_couleurs = QPushButton('Inversion', self)
		self.bouton_inversion_couleurs.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		# Connexion du bouton Inversion à la méthode inversion_couleurs() lorsqu'on clique sur le bouton
		self.bouton_inversion_couleurs.clicked.connect(self.inverser_couleurs)
		self.bouton_inversion_couleurs.move(int((self.frameGeometry().width() - self.bouton_reset.width()) / 2), 550)
  
		# Création d'un label zoom image sans empilements
  
		self.label_zoom_image_sans_empilements = QLabel("Zoom Image Originale", self)
		self.label_zoom_image_sans_empilements.setGeometry(0, 0, 170, 30)
		self.label_zoom_image_sans_empilements.move(231, 495)
		self.label_zoom_image_sans_empilements.setStyleSheet("background-color: rgb(61, 61, 61); font-size: 10pt; color: rgb(210, 210, 210);")				
		self.label_zoom_image_sans_empilements.setAlignment(Qt.AlignmentFlag.AlignHCenter)
  
		# Création d'un label graduations zoom image sans empilements
  
		# Le titre du QLabel contient un espacement de caractères de telle sorte que le x1 soit tout à gauche du Zoom et que le x100 soit tout à droite du Zoom
		self.label_graduations_zoom_image_sans_empilements = QLabel("x1                           x100", self)
		self.label_graduations_zoom_image_sans_empilements.setGeometry(0, 0, 170, 15)
		self.label_graduations_zoom_image_sans_empilements.move(231, 560)
		self.label_graduations_zoom_image_sans_empilements.setStyleSheet("background-color: rgb(61, 61, 61); font-size: 10pt; color: rgb(210, 210, 210);")				
		self.label_graduations_zoom_image_sans_empilements.setAlignment(Qt.AlignmentFlag.AlignHCenter)
  
		# Création d'un zoom pour l'image sans empilements
  
		self.zoom_image_sans_empilements = QSlider(self)
		# Géométrie du QSlider
		self.zoom_image_sans_empilements.setGeometry(0, 0, 130, 30)
		# Valeur minimale du QSlider (ici 1 pour un zoom x1)
		self.zoom_image_sans_empilements.setMinimum(1)
		# Valeur maximale du QSlider (ici 100 pour un zoom x100)
		self.zoom_image_sans_empilements.setMaximum(100)
		# Par défaut, le curseur du QSlider est placé sur le zoom x1
		self.zoom_image_sans_empilements.setValue(1)
		# A chaque déplacement de curseur du QSlider, le pas du curseur est de 10
		self.zoom_image_sans_empilements.setSingleStep(10)
		# Les graduations du QSlider sont positionnées en-dessous du QSlider
		self.zoom_image_sans_empilements.setTickPosition(QSlider.TickPosition.TicksBelow)
		# L'orientation du QSlider est horizontale
		self.zoom_image_sans_empilements.setOrientation(Qt.Orientation.Horizontal)
		# Chaque graduation du QSlider est de 10
		self.zoom_image_sans_empilements.setTickInterval(10)
		# Position du QSlider
		self.zoom_image_sans_empilements.move(int((self.frameGeometry().width() - self.bouton_reset.width()) / 2) - 200, 525)
		self.zoom_image_sans_empilements.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")		
		# Connexion du QSlider à la méthode zoomer() si la valeur change lorsque le curseur se déplace
		self.zoom_image_sans_empilements.valueChanged.connect(self.zoomer)
  
		# Création d'un label zoom image avec empilement
  
		self.label_zoom_image_avec_empilement = QLabel("Zoom Image Empilée", self)
		self.label_zoom_image_avec_empilement.setGeometry(0, 0, 170, 30)
		self.label_zoom_image_avec_empilement.move(601, 495)
		self.label_zoom_image_avec_empilement.setStyleSheet("background-color: rgb(61, 61, 61); font-size: 10pt; color: rgb(210, 210, 210);")				
		self.label_zoom_image_avec_empilement.setAlignment(Qt.AlignmentFlag.AlignHCenter)
  
		# Création d'un label graduations zoom image avec empilement
  
		self.label_graduations_zoom_image_avec_empilement = QLabel("x1                           x100", self)
		self.label_graduations_zoom_image_avec_empilement.setGeometry(0, 0, 170, 15)
		self.label_graduations_zoom_image_avec_empilement.move(601, 560)
		self.label_graduations_zoom_image_avec_empilement.setStyleSheet("background-color: rgb(61, 61, 61); font-size: 10pt; color: rgb(210, 210, 210);")				
		self.label_graduations_zoom_image_avec_empilement.setAlignment(Qt.AlignmentFlag.AlignHCenter)
  
		# Création d'un zoom pour l'image avec empilement
  
		self.zoom_image_avec_empilement = QSlider(self)
		self.zoom_image_avec_empilement.setGeometry(0, 0, 130, 30)
		self.zoom_image_avec_empilement.setMinimum(1)
		self.zoom_image_avec_empilement.setMaximum(100)
		self.zoom_image_avec_empilement.setValue(1)
		self.zoom_image_avec_empilement.setSingleStep(10)
		self.zoom_image_avec_empilement.setTickPosition(QSlider.TickPosition.TicksBelow)
		self.zoom_image_avec_empilement.setOrientation(Qt.Orientation.Horizontal)
		self.zoom_image_avec_empilement.setTickInterval(10)
		self.zoom_image_avec_empilement.move(int((self.frameGeometry().width() - self.bouton_reset.width()) / 2) + 170, 525)
		self.zoom_image_avec_empilement.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")		
		self.zoom_image_avec_empilement.valueChanged.connect(self.zoomer)
  
		# Création d'un label options
  
		self.label_options = QLabel("                 Options", self)
		self.label_options.setGeometry(0, 0, 170, 180)
		self.label_options.move(813, 25)
		self.label_options.setStyleSheet("background-color: rgb(61, 61, 61); border: 2px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")				
		self.label_options.setAlignment(Qt.AlignmentFlag.AlignTop)
  
		# Création d'un bouton ouvrir dossier
  
		self.bouton_ouvrir_dossier = QPushButton('Charger Dossier', self)
		self.bouton_ouvrir_dossier.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.bouton_ouvrir_dossier.clicked.connect(self.charger_images_a_empiler)
		self.bouton_ouvrir_dossier.move(850, 70)
  
		# Création d'un bouton sauvegarder
  
		self.bouton_sauvegarder = QPushButton('Sauvegarder Image Empilée', self)
		self.bouton_sauvegarder.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 5pt; color: rgb(210, 210, 210);")
		self.bouton_sauvegarder.clicked.connect(self.sauvegarder)
		self.bouton_sauvegarder.move(850, 140)
  
		# Création d'un label traitement images
  
		self.label_traitement = QLabel("    Traitement Images FITS", self)
		self.label_traitement.setGeometry(0, 0, 170, 200)
		self.label_traitement.move(813, 200)
		self.label_traitement.setStyleSheet("background-color: rgb(61, 61, 61); border: 2px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")				
		self.label_traitement.setAlignment(Qt.AlignmentFlag.AlignTop)
  
		# Création d'un bouton empilement somme
  
		self.bouton_empilement_somme = QPushButton('Empilement Par Somme', self)
		self.bouton_empilement_somme.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 5pt; color: rgb(210, 210, 210);")
		self.bouton_empilement_somme.clicked.connect(self.faire_empilement_somme)
		self.bouton_empilement_somme.move(850, 250)
  
		# Création d'un bouton empilement médiane
  
		self.bouton_empilement_mediane = QPushButton('Empilement Par Médiane', self)
		self.bouton_empilement_mediane.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 5pt; color: rgb(210, 210, 210);")
		self.bouton_empilement_mediane.clicked.connect(self.faire_empilement_mediane)
		self.bouton_empilement_mediane.move(850, 300)
  
		# Création d'un bouton empilement moyenne
  
		self.bouton_empilement_moyenne = QPushButton('Empilement Par Moyenne', self)
		self.bouton_empilement_moyenne.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 5pt; color: rgb(210, 210, 210);")
		self.bouton_empilement_moyenne.clicked.connect(self.faire_empilement_moyenne)
		self.bouton_empilement_moyenne.move(850, 350)
  
		# Création d'un label images à empiler
  
		self.label_images_a_empiler = QLabel("         Images A Empiler", self)
		self.label_images_a_empiler.setGeometry(0, 0, 170, 195)
		self.label_images_a_empiler.move(813, 390)
		self.label_images_a_empiler.setStyleSheet("background-color: rgb(61, 61, 61); border: 2px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")				
		self.label_images_a_empiler.setAlignment(Qt.AlignmentFlag.AlignTop)

		# Création d'une QListWidget
  
		self.liste = QListWidget(self)
		self.liste.setGeometry(0, 0, 143, 150)
		self.liste.move(826, 424)
		self.liste.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 10pt; color: rgb(0, 0, 0);")				
  
		self.scrollbar = QScrollBar(self)
		# Ajout d'une barre de scrolling verticale à la QListWidget
		self.liste.setVerticalScrollBar(self.scrollbar)
		# Ajout d'une barre de scrolling horizontale à la QListWidget
		self.liste.setHorizontalScrollBar(self.scrollbar)
		# La barre de scrolling verticale apparaît si nécessaire
		self.liste.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
		# La barre de scrolling horizontale apparaît si nécessaire
		self.liste.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
  
		# Création d'un label informations image
  
		self.label_informations_image = QLabel("   Informations Sur l'Image", self)
		self.label_informations_image.setGeometry(0, 0, 170, 370)
		self.label_informations_image.move(17, 25)
		self.label_informations_image.setStyleSheet("background-color: rgb(61, 61, 61); border: 2px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")				
		self.label_informations_image.setAlignment(Qt.AlignmentFlag.AlignTop)
  
		# Création d'un label informations
  
		self.liste_informations = QListWidget(self)
		self.liste_informations.setGeometry(0, 0, 160, 340)
		self.liste_informations.move(23, 50)
		self.liste_informations.setStyleSheet("background-color: rgb(61, 61, 61); font-size: 10pt; color: rgb(210, 210, 210);")				
  
		# Création d'un label
  
		self.label = QLabel(self)
		self.label.setGeometry(0, 0, 170, 192)
		self.label.move(17, 393)
		self.label.setStyleSheet("background-color: rgb(61, 61, 61); border: 2px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")				
		self.label.setAlignment(Qt.AlignmentFlag.AlignTop)
  
		# Création d'un bouton à propos
  
		self.bouton_a_propos = QPushButton('A propos', self)
		self.bouton_a_propos.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.bouton_a_propos.clicked.connect(self.a_propos)
		self.bouton_a_propos.move(50, 420)
  
		# Création d'un bouton aide
  
		self.bouton_aide = QPushButton('Aide', self)
		self.bouton_aide.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.bouton_aide.clicked.connect(self.aide)
		self.bouton_aide.move(50, 480)
  
		# Création des thèmes
  
		self.themes = QComboBox(self)
		self.themes.setStyleSheet("background-color: rgb(51, 51, 51); border: 1px solid rgb(0, 0, 0); font-size: 7pt; color: rgb(210, 210, 210);")
		self.themes.addItem("Thème Original")
		self.themes.addItem("Lo-Fi Vibes")
		self.themes.addItem("Pour Les Garçons")
		self.themes.addItem("Pour Les Filles")
		self.themes.addItem("Sobriété Energétique")
		# Connexion de la QComboBox à la méthode changer_theme() lorsqu'on clique sur un de ses éléments
		self.themes.textActivated.connect(self.changer_theme)
		self.themes.move(50, 540)

		# Autres attributs

		self.chemin_dossier = ""
		self.liste_ndarray = []
		self.empilement_par_somme = []
		self.empilement_par_mediane = []
		self.empilement_par_moyenne = []
		self.image_initiale = ""
		self.empilement = ""
  

	# Définition des méthodes


	# Méthode connectée à un QPushButton qui ajoute et affiche les noms des chemins de fichiers dans la QListWidget et qui définit le chemin du dossier à charger
	def charger_images_a_empiler(self) :
		# Si l'utilisateur ne quitte pas la fenêtre de sélection de dossier
		try :
			# On sélectionne le chemin du dossier à l'aide de QFileDialog
			self.chemin_dossier = QFileDialog.getExistingDirectory(self)
			# On liste tous les noms des chemins de fichiers du dossier à l'aide de os
			liste_noms_fichiers = os.listdir(self.chemin_dossier)
			# Si la QListWidget est vide, on remplit la colonne 0 de la QListWidget des noms des chemins de fichiers du dossier ayant pour extension .fits
			if len(self.liste) == 0 :
				# On parcourt chaque élément de la liste des noms des chemins de fichiers
				for i in range(0, len(liste_noms_fichiers)) :
					# Si un élément de la liste des noms des chemins de fichiers n'a pas l'extension .fits, on le retire de cette liste
					if liste_noms_fichiers[i][-5:] != ".fits" :
						liste_noms_fichiers.remove(liste_noms_fichiers[i])
					# Si un élément de la liste des noms des chemins de fichiers a l'extension .fits, on l'ajoute à la colonne 0 de la QListWidget
					elif liste_noms_fichiers[i][-5:] == ".fits" :
						self.liste.insertItem(i, liste_noms_fichiers[i])
			# Si la QListWidget n'est pas vide, et donc si l'utilisateur a déjà chargé un dossier, la colonne 0 de la QListWidget se vide et se remplit de nouveau des noms des fichiers du nouveau dossier ayant pour extension .fits
			elif len(self.liste) != 0 :
				for i in range(0, len(self.liste)) :
					self.liste.takeItem(0)
				for i in range(0, len(liste_noms_fichiers)) :
					# Si un élément de la liste des noms des chemins de fichiers n'a pas l'extension .fits, on le retire de cette liste
					if liste_noms_fichiers[i][-5:] != ".fits" :
						liste_noms_fichiers.remove(liste_noms_fichiers[i])
					# Si un élément de la liste des noms des chemins de fichiers a l'extension .fits, on l'ajoute à la colonne 0 de la QListWidget
					elif liste_noms_fichiers[i][-5:] == ".fits" :
						self.liste.insertItem(i, liste_noms_fichiers[i])
		# Sinon
		except :
			return "Erreur"


	# Méthode qui ajoute les éléments de la QListWidget (noms des chemins de fichiers) dans une liste de chaînes de caractères
	def charger_dossier(self) :
		liste_noms_fichiers = []
		if len(self.liste) != 0 :
			for i in range(0, len(self.liste)) :
				liste_noms_fichiers.append(self.liste.item(i).text())
		return liste_noms_fichiers


	# Méthode qui retourne une liste contenant les images fits à partir des noms des chemins de fichiers du dossier chargé
	def charger_liste_fichiers(self, liste_noms_fichiers) :
		liste_de_fichiers = []
		for i in range(0, len(liste_noms_fichiers)) :
			# On récupère les images FITS qui sont des fichiers de données et on les ajoute dans la liste de fichiers
			# get_pkg_data_filename() récupère une image FITS à partir des emplacements standards du paquet en retournant un nom de fichier local pour les données sous la forme d'un string
			liste_de_fichiers.append(get_pkg_data_filename(self.chemin_dossier + "\\" + liste_noms_fichiers[i]))
		return liste_de_fichiers


	# Méthode permettant d'ajouter des tableaux numpy ndarray à une liste à partir des images fits
	def charger_liste_ndarray(self, liste_de_fichiers) :
		self.liste_ndarray = [fits.getdata(image) for image in liste_de_fichiers]
	
	
	# Méthode permettant de faire un empilement par somme des images fits
	def empilement_somme(self) :
		# On utilise np.sum avec axis = 0 dans la liste pour faire la somme de toutes les lignes de chaque ndarray représentant chaque image fits et on la stocke dans un nouveau ndarray
		self.empilement_par_somme = np.sum(self.liste_ndarray, axis = 0)
		return "somme"

	# Méthode permettant de faire un empilement par médiane des images fits
	def empilement_mediane(self) :
		# On utilise np.median avec axis = 0 dans la liste pour faire la médiane de toutes les lignes de chaque ndarray représentant chaque image fits et on la stocke dans un nouveau ndarray
		self.empilement_par_mediane = np.median(self.liste_ndarray, axis = 0)
		return "médiane"


	# Méthode permettant de faire un empilement par moyenne des images fits
	def empilement_moyenne(self) :
		# On utilise np.mean avec axis = 0 dans la liste pour faire la moyenne de toutes les lignes de chaque ndarray représentant chaque image fits et on la stocke dans un nouveau ndarray
		self.empilement_par_moyenne = np.mean(self.liste_ndarray, axis = 0)
		return "moyenne"
  
  
	# Méthode qui affiche l'image fits sans empilements et l'image fits avec empilement à partir de tableaux numpy ndarray et du nom de la méthode d'empilement
	def afficher(self, methode_empilement, nom_methode) :
		# On ajoute un graphique dans la figure qui est l'image sans empilements
		self.figure_images.add_subplot(2, 2, 1)
		self.figure_images.add_subplot(2, 2, 1).set_title("Image sans empilements")
		# On affiche le graphique de la figure qui est le tableau numpy ndarray représentant l'image sans empilements
		plt.imshow(self.liste_ndarray[0])
		plt.axis("Off")
		# L'axe x correspond à la longueur du tableau numpy ndarray
		plt.xlim(0, len(self.liste_ndarray[0][0]))
		# L'axe y correspond à la taille du tableau numpy ndarray divisé par sa longueur
		plt.ylim(0, self.liste_ndarray[0].size//len(self.liste_ndarray[0][0]))
		plt.colorbar(location="bottom")
		self.figure_images.add_subplot(2, 2, 2)
		self.figure_images.add_subplot(2, 2, 2).set_title("Empilement par " + nom_methode)
		plt.imshow(methode_empilement)
		plt.colorbar(location="bottom")
		plt.axis("Off")
		plt.xlim(0, len(self.liste_ndarray[0][0]))
		plt.ylim(0, self.liste_ndarray[0].size//len(self.liste_ndarray[0][0]))
   
   
	# Méthode connectée à un QPushButton qui permet d'afficher l'image fits avec un empilement par somme sur le canevas et d'afficher les informations de l'image
	def faire_empilement_somme(self):
		# Si l'utilisateur a fermé la fenêtre de sélection de dossier ou que l'utilisateur clique sur un empilement sans avoir chargé de dossier
		if self.chemin_dossier == "Erreur" or self.chemin_dossier == "" :
			print("Erreur")
		# Sinon
		else :
			self.figure_images.clear()
			# On ajoute les éléments de la QListWidget (noms des chemins de fichiers) dans une liste de chaînes de caractères
			liste_noms_fichiers = self.charger_dossier()
			# On créé une liste contenant les images fits à partir des noms des chemins de fichiers du dossier chargé
			liste_de_fichiers = self.charger_liste_fichiers(liste_noms_fichiers)
			# On ajoute des tableaux numpy ndarray à la liste à partir des images fits
			self.charger_liste_ndarray(liste_de_fichiers)
			# On fait un empilement par somme
			nom_methode = self.empilement_somme()
			# On affiche l'image sans empilements et l'image avec empilement par somme sur le canevas
			self.afficher(self.empilement_par_somme, nom_methode)
			# On signale qu'on a bien une image sans empilements
			self.image_initiale = "image"
			# On signale que l'empilement est un empilement par somme
			self.empilement = "somme"
			# On ouvre le premier nom de chemin de fichier de la liste de fichiers pour avoir les informations sur la première image FITS
			informations_image = fits.open(liste_de_fichiers[0])
			# S'il y a déjà des informations sur une image, on supprime ces informations
			if len(self.liste_informations) != 0 :
				for i in range(0, len(self.liste_informations)) :
					self.liste_informations.takeItem(0)
			# On initialise une variable pour représenter la ligne de la QListWidget
			i = 0
			# On parcourt toutes les clés du dictionnaire représentant les informations de la première image FITS
			for cle in informations_image.fileinfo(0) :
				# On ajoute les informations de la première image FITS à la QListWidget ligne par ligne
				self.liste_informations.insertItem(i, str(informations_image.fileinfo(0)[cle]))
				# On incrémente donc de 1 pour pouvoir ajouter les informations ligne par ligne
				i += 1
			# On affiche le chemin du dossier sélectionné sur le label
			self.label_chemin_fichier.setText(self.chemin_dossier)
			# On rafraichit le canevas
			self.canvas_images.draw()
   
	
	# Méthode connectée à un QPushButton qui permet d'afficher l'image fits avec un empilement par médiane sur le canevas et d'afficher les informations de l'image
	def faire_empilement_mediane(self):
		if self.chemin_dossier == "Erreur" or self.chemin_dossier == "" :
			print("Erreur")
		else :
			self.figure_images.clear()
			liste_noms_fichiers = self.charger_dossier()
			liste_de_fichiers = self.charger_liste_fichiers(liste_noms_fichiers)
			self.charger_liste_ndarray(liste_de_fichiers)
			nom_methode = self.empilement_mediane()
			self.afficher(self.empilement_par_mediane, nom_methode)
			self.image_initiale = "image"
			self.empilement = "médiane"
			informations_image = fits.open(liste_de_fichiers[0])
			i = 0
			if len(self.liste_informations) != 0 :
				for i in range(0, len(self.liste_informations)) :
					self.liste_informations.takeItem(0)
					i += 1
			i = 0
			for cle in informations_image.fileinfo(0) :
				self.liste_informations.insertItem(i, str(informations_image.fileinfo(0)[cle]))
				i += 1
			self.label_chemin_fichier.setText(self.chemin_dossier)
			self.canvas_images.draw()
   
	
	# Méthode connectée à un QPushButton qui permet d'afficher l'image fits avec un empilement par moyenne sur le canevas et d'afficher les informations de l'image
	def faire_empilement_moyenne(self):
		if self.chemin_dossier == "Erreur" or self.chemin_dossier == "" :
			print("Erreur")
		else :
			self.figure_images.clear()
			liste_noms_fichiers = self.charger_dossier()
			liste_de_fichiers = self.charger_liste_fichiers(liste_noms_fichiers)
			self.charger_liste_ndarray(liste_de_fichiers)
			nom_methode = self.empilement_moyenne()
			self.afficher(self.empilement_par_moyenne, nom_methode)
			self.image_initiale = "image"
			self.empilement = "moyenne"
			informations_image = fits.open(liste_de_fichiers[0])
			i = 0
			if len(self.liste_informations) != 0 :
				for i in range(0, len(self.liste_informations)) :
					self.liste_informations.takeItem(0)
					i += 1
			i = 0
			for cle in informations_image.fileinfo(0) :
				self.liste_informations.insertItem(i, str(informations_image.fileinfo(0)[cle]))
				i += 1
			self.label_chemin_fichier.setText(self.chemin_dossier)
			self.canvas_images.draw()
  
	
	# Méthode connectée à un QPushButton qui permet de sauvegarder une image FITS empilée dans un dossier
	def sauvegarder(self) :
		# On sélectionne le chemin du dossier
		chemin_sauvegarde = QFileDialog.getExistingDirectory(self)
		# Si l'empilement est un empilement par somme
		if self.empilement == "somme" :
			# On convertit le tableau numpy ndarray représentant l'image FITS empilée en une image FITS
			image = Image.fromarray(self.empilement_par_somme, "RGB")
			nom_image = "Image_empilement_somme.fits"
			# On sauvegarde l'image dans le dossier
			image.save(chemin_sauvegarde + "\\" + nom_image)
		# Si l'empilement est un empilement par médiane
		elif self.empilement == "médiane" :
			image = Image.fromarray(self.empilement_par_mediane, "RGB")
			nom_image = "Image_empilement_mediane.fits"
			image.save(chemin_sauvegarde + "\\" + nom_image)
		# Si l'empilement est un empilement par moyenne
		elif self.empilement == "moyenne" :
			image = Image.fromarray(self.empilement_par_moyenne, "RGB")
			nom_image = "Image_empilement_moyenne.fits"
			image.save(chemin_sauvegarde + "\\" + nom_image)
  
	
	# Méthode connectée à un QSlider qui permet de zoomer sur un des graphiques de la figure
	def zoomer(self) :
		# Si on a bien une image sans empilements
		if self.image_initiale == "image" :
			# On rafraichit
			self.figure_images.add_subplot(2, 2, 1).clear()
			self.figure_images.add_subplot(2, 2, 1)
			# On affiche le graphique de la figure qui est le tableau numpy ndarray représentant l'image sans empilements
			plt.imshow(self.liste_ndarray[0])
			plt.axis("Off")
			# On zoome / dézoome en modifiant la longueur de l'axe x du graphique en divisant la longueur du tableau par la valeur du QSlider 
			plt.xlim(0, len(self.liste_ndarray[0][0])//self.zoom_image_sans_empilements.value())
			# On zoome / dézoome en modifiant la longueur de l'axe y du graphique en divisant la hauteur du tableau par la valeur du QSlider
			plt.ylim(0, (self.liste_ndarray[0].size//len(self.liste_ndarray[0][0]))//self.zoom_image_sans_empilements.value())
			plt.colorbar(location="bottom")
			# On rafraichit
			self.canvas_images.draw()
		if self.empilement == "somme" :
			self.figure_images.add_subplot(2, 2, 2).clear()
			self.figure_images.add_subplot(2, 2, 2)
			plt.imshow(self.empilement_par_somme)
			plt.axis("Off")
			plt.xlim(0, len(self.liste_ndarray[0][0])//self.zoom_image_avec_empilement.value())
			plt.ylim(0, (self.liste_ndarray[0].size//len(self.liste_ndarray[0][0]))//self.zoom_image_avec_empilement.value())
			plt.colorbar(location="bottom")
			self.canvas_images.draw()
		if self.empilement == "médiane" :
			self.figure_images.add_subplot(2, 2, 2).clear()
			self.figure_images.add_subplot(2, 2, 2)
			plt.imshow(self.empilement_par_mediane)
			plt.axis("Off")
			plt.xlim(0, len(self.liste_ndarray[0][0])//self.zoom_image_avec_empilement.value())
			plt.ylim(0, (self.liste_ndarray[0].size//len(self.liste_ndarray[0][0]))//self.zoom_image_avec_empilement.value())
			plt.colorbar(location="bottom")
			self.canvas_images.draw()
		if self.empilement == "moyenne" :
			self.figure_images.add_subplot(2, 2, 2).clear()
			self.figure_images.add_subplot(2, 2, 2)
			plt.imshow(self.empilement_par_moyenne)
			plt.axis("Off")
			plt.xlim(0, len(self.liste_ndarray[0][0])//self.zoom_image_avec_empilement.value())
			plt.ylim(0, (self.liste_ndarray[0].size//len(self.liste_ndarray[0][0]))//self.zoom_image_avec_empilement.value())
			plt.colorbar(location="bottom")
			self.canvas_images.draw()
   
  
	# Méthode connectée à un QPushButton qui permet d'afficher une sous-fenêtre A propos avec du texte et des sauts à la ligne
	def a_propos(self) :
		fenetre_a_propos = QMdiSubWindow(self)
		fenetre_a_propos.setWindowTitle("A Propos")
		fenetre_a_propos.setFixedSize(400, 400)
		fenetre_a_propos.setStyleSheet("color: rgb(210, 210, 210);")
		texte_a_propos = QLabel("Logiciel de Stacking créé par Alexandre Pap et Alban Pruvost en BUT2 pour la SAE C2", fenetre_a_propos)
		texte_a_propos.setWordWrap(True)
		texte_a_propos.setGeometry(0, 0, 400, 400)
		fenetre_a_propos.setWidget(texte_a_propos)
		fenetre_a_propos.move(0, 0)
		fenetre_a_propos.show()
  
	
	# Méthode connectée à un QPushButton qui permet d'afficher une sous-fenêtre Aide avec du texte et des sauts à la ligne
	def aide(self) :
		fenetre_aide = QMdiSubWindow(self)
		fenetre_aide.setWindowTitle("Aide")
		fenetre_aide.setFixedSize(400, 400)
		fenetre_aide.setStyleSheet("color: rgb(210, 210, 210);")
		texte_aide = QLabel("Si vous avez un dossier contenant des images FITS à empiler, veillez à les mettre dans le dossier bibliotheque du dossier où se trouve également l'installeur FitsStacker.exe . Appuyez sur le bouton Charger Dossier pour charger un dossier de votre choix contenant des images FITS à empiler. Sélectionnez ensuite une des trois méthodes d'empilement proposées. Une image FITS de votre dossier sans empilements et une image avec l'empilement sélectionné apparaîtront sur le canevas au centre de la fenêtre. Cliquez sur Sauvegarder pour sauvegarder l'image empilée. Vous pouvez zoomer sur une des deux images, appliquer des filtres ou faire un reset. Vous pouvez aussi changer le thème de FitsStacker, ou cliquer sur A propos ou Aide pour toute information complémentaire. Bonne prise en main =)", fenetre_aide)
		texte_aide.setWordWrap(True)
		texte_aide.setGeometry(10, 10, 390, 190)
		fenetre_aide.setWidget(texte_aide)
		fenetre_aide.move(400, 0)
		fenetre_aide.show()
  
	
	# Méthode connectée à une QComboBox qui permet de modifier la couleur de la fenêtre, de ses sous-fenêtres et de ses éléments graphiques
	def changer_theme(self) :
		couleur1 = "rgb(61, 61, 61)"
		couleur2 = "rgb(51, 51, 51)"
  
		if self.themes.currentText() == "Thème Original" :
			couleur1 = "rgb(61, 61, 61)"
			couleur2 = "rgb(51, 51, 51)"
		elif self.themes.currentText() == "Lo-Fi Vibes" :
			couleur1 = "rgb(102, 78, 11)"
			couleur2 = "rgb(128, 100, 23)"
		elif self.themes.currentText() == "Pour Les Garçons" :
			couleur1 = "rgb(255, 88, 250)"
			couleur2 = "rgb(255, 176, 253)"
		elif self.themes.currentText() == "Pour Les Filles" :
			couleur1 = "rgb(68, 54, 255)"
			couleur2 = "rgb(172, 166, 255)"
		# Macron sera content
		elif self.themes.currentText() == "Sobriété Energétique" :
			sys.exit()
      
		self.setStyleSheet("background-color:" + couleur1 + ";")
		self.label_canvas_et_zoom.setStyleSheet("background-color:" + couleur1 + "; border: 2px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.label_chemin_fichier.setStyleSheet("background-color:" + couleur2 + "; border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.bouton_reset.setStyleSheet("background-color:" + couleur1 + "; border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.bouton_floutage.setStyleSheet("background-color:" + couleur1 + "; border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.bouton_inversion_couleurs.setStyleSheet("background-color:" + couleur1 + "; border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.label_zoom_image_sans_empilements.setStyleSheet("background-color:" + couleur1 + "; font-size: 10pt; color: rgb(210, 210, 210);")
		self.label_graduations_zoom_image_sans_empilements.setStyleSheet("background-color:" + couleur1 + "; font-size: 10pt; color: rgb(210, 210, 210);")
		self.zoom_image_sans_empilements.setStyleSheet("background-color:" + couleur2 + "; border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.label_zoom_image_avec_empilement.setStyleSheet("background-color:" + couleur1 + "; font-size: 10pt; color: rgb(210, 210, 210);")
		self.label_graduations_zoom_image_avec_empilement.setStyleSheet("background-color:" + couleur1 + "; font-size: 10pt; color: rgb(210, 210, 210);")
		self.zoom_image_avec_empilement.setStyleSheet("background-color:" + couleur2 + "; border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.label_options.setStyleSheet("background-color:" + couleur1 + "; border: 2px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.bouton_ouvrir_dossier.setStyleSheet("background-color:" + couleur2 + "; border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.bouton_sauvegarder.setStyleSheet("background-color:" + couleur2 + "; border: 1px solid rgb(0, 0, 0); font-size: 5pt; color: rgb(210, 210, 210);")
		self.label_traitement.setStyleSheet("background-color:" + couleur1 + "; border: 2px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.bouton_empilement_somme.setStyleSheet("background-color:" + couleur2 + "; border: 1px solid rgb(0, 0, 0); font-size: 5pt; color: rgb(210, 210, 210);")
		self.bouton_empilement_mediane.setStyleSheet("background-color:" + couleur2 + "; border: 1px solid rgb(0, 0, 0); font-size: 5pt; color: rgb(210, 210, 210);")
		self.bouton_empilement_moyenne.setStyleSheet("background-color:" + couleur2 + "; border: 1px solid rgb(0, 0, 0); font-size: 5pt; color: rgb(210, 210, 210);")
		self.label_images_a_empiler.setStyleSheet("background-color:" + couleur1 + "; border: 2px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.liste.setStyleSheet("background-color: rgb(255, 255, 255); font-size: 10pt; color: rgb(0, 0, 0);")
		self.label_informations_image.setStyleSheet("background-color:" + couleur1 + "; border: 2px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.liste_informations.setStyleSheet("background-color:" + couleur1 + "; font-size: 10pt; color: rgb(210, 210, 210);")
		self.label.setStyleSheet("background-color:" + couleur1 + "; border: 2px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.bouton_a_propos.setStyleSheet("background-color:" + couleur2 + "; border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.bouton_aide.setStyleSheet("background-color:" + couleur2 + "; border: 1px solid rgb(0, 0, 0); font-size: 10pt; color: rgb(210, 210, 210);")
		self.themes.setStyleSheet("background-color:" + couleur2 + "; border: 1px solid rgb(0, 0, 0); font-size: 7pt; color: rgb(210, 210, 210);")
		
  
	# Méthode connectée à un QPushButton qui permet de flouter l'image fits avec empilement
	def flouter(self) :
		if self.empilement == "somme" :
			# Pour chaque ligne
			for i in range(1, self.empilement_par_somme.shape[0] - 1) :
				# Pour chaque colonne
				for j in range(1, self.empilement_par_somme.shape[0] - 1) :
					# On applique la formule du floutage pour chaque pixel suivant ses pixels voisins
					self.empilement_par_somme[i, j] = (4 * self.empilement_par_somme[i, j] + self.empilement_par_somme[i + 1, j] + self.empilement_par_somme[i - 1, j] + self.empilement_par_somme[i, j + 1] + self.empilement_par_somme[i, j - 1]) / 8.0
			# On rafraichit
			self.figure_images.add_subplot(2, 2, 2).clear()
			self.figure_images.add_subplot(2, 2, 2)
			# On affiche le graphique de la figure qui est le tableau numpy ndarray représentant l'image avec empilement par somme
			plt.imshow(self.empilement_par_somme)
			# L'axe x correspond à la longueur du tableau numpy ndarray
			plt.xlim(0, len(self.liste_ndarray[0][0]))
			# L'axe y correspond à la taille du tableau numpy ndarray divisé par sa longueur
			plt.ylim(0, self.liste_ndarray[0].size//len(self.liste_ndarray[0][0]))
			plt.colorbar(location="bottom")
			# On rafraichit
			self.canvas_images.draw()
		elif self.empilement == "médiane" :
    			# Pour chaque ligne
			for i in range(1, self.empilement_par_mediane.shape[0] - 1) :
				# Pour chaque colonne
				for j in range(1, self.empilement_par_mediane.shape[0] - 1) :
					# On applique la formule du floutage pour chaque pixel suivant ses pixels voisins
					self.empilement_par_mediane[i, j] = (4 * self.empilement_par_mediane[i, j] + self.empilement_par_mediane[i + 1, j] + self.empilement_par_mediane[i - 1, j] + self.empilement_par_mediane[i, j + 1] + self.empilement_par_mediane[i, j - 1]) / 8.0
			# On rafraichit
			self.figure_images.add_subplot(2, 2, 2).clear()
			self.figure_images.add_subplot(2, 2, 2)
			# On affiche le graphique de la figure qui est le tableau numpy ndarray représentant l'image avec empilement par médiane
			plt.imshow(self.empilement_par_mediane)
			# L'axe x correspond à la longueur du tableau numpy ndarray
			plt.xlim(0, len(self.liste_ndarray[0][0]))
			# L'axe y correspond à la taille du tableau numpy ndarray divisé par sa longueur
			plt.ylim(0, self.liste_ndarray[0].size//len(self.liste_ndarray[0][0]))
			plt.colorbar(location="bottom")
			# On rafraichit
			self.canvas_images.draw()
		elif self.empilement == "moyenne" :
    			# Pour chaque ligne
			for i in range(1, self.empilement_par_moyenne.shape[0] - 1) :
				# Pour chaque colonne
				for j in range(1, self.empilement_par_moyenne.shape[0] - 1) :
					# On applique la formule du floutage pour chaque pixel suivant ses pixels voisins
					self.empilement_par_moyenne[i, j] = (4 * self.empilement_par_moyenne[i, j] + self.empilement_par_moyenne[i + 1, j] + self.empilement_par_moyenne[i - 1, j] + self.empilement_par_moyenne[i, j + 1] + self.empilement_par_moyenne[i, j - 1]) / 8.0
			# On rafraichit
			self.figure_images.add_subplot(2, 2, 2).clear()
			self.figure_images.add_subplot(2, 2, 2)
			# On affiche le graphique de la figure qui est le tableau numpy ndarray représentant l'image avec empilement par moyenne
			plt.imshow(self.empilement_par_moyenne)
			# L'axe x correspond à la longueur du tableau numpy ndarray
			plt.xlim(0, len(self.liste_ndarray[0][0]))
			# L'axe y correspond à la taille du tableau numpy ndarray divisé par sa longueur
			plt.ylim(0, self.liste_ndarray[0].size//len(self.liste_ndarray[0][0]))
			plt.colorbar(location="bottom")
			# On rafraichit
			self.canvas_images.draw()


	# Méthode connectée à un QPushButton qui permet d'inverser les couleurs de l'image fits avec empilement
	def inverser_couleurs(self) :
		if self.empilement == "somme" :
    		# Pour chaque ligne
			for i in range(1, self.empilement_par_somme.shape[0] - 1) :
				# Pour chaque colonne
				for j in range(1, self.empilement_par_somme.shape[1] - 1) :
					self.empilement_par_somme[i, j] = 255 - self.empilement_par_somme[i, j]
			# On rafraichit
			self.figure_images.add_subplot(2, 2, 2).clear()
			self.figure_images.add_subplot(2, 2, 2)
			# On affiche le graphique de la figure qui est le tableau numpy ndarray représentant l'image avec empilement par somme
			plt.imshow(self.empilement_par_somme)
			# L'axe x correspond à la longueur du tableau numpy ndarray
			plt.xlim(0, len(self.liste_ndarray[0][0]))
			# L'axe y correspond à la taille du tableau numpy ndarray divisé par sa longueur
			plt.ylim(0, self.liste_ndarray[0].size//len(self.liste_ndarray[0][0]))
			plt.colorbar(location="bottom")
			# On rafraichit
			self.canvas_images.draw()
		elif self.empilement == "médiane" :
    		# Pour chaque ligne
			for i in range(1, self.empilement_par_mediane.shape[0] - 1) :
				# Pour chaque colonne
				for j in range(1, self.empilement_par_mediane.shape[1] - 1) :
					self.empilement_par_mediane[i, j] = 255 - self.empilement_par_mediane[i, j]
			# On rafraichit
			self.figure_images.add_subplot(2, 2, 2).clear()
			self.figure_images.add_subplot(2, 2, 2)
			# On affiche le graphique de la figure qui est le tableau numpy ndarray représentant l'image avec empilement par médiane
			plt.imshow(self.empilement_par_mediane)
			# L'axe x correspond à la longueur du tableau numpy ndarray
			plt.xlim(0, len(self.liste_ndarray[0][0]))
			# L'axe y correspond à la taille du tableau numpy ndarray divisé par sa longueur
			plt.ylim(0, self.liste_ndarray[0].size//len(self.liste_ndarray[0][0]))
			plt.colorbar(location="bottom")
			# On rafraichit
			self.canvas_images.draw()
		elif self.empilement == "moyenne" :
    		# Pour chaque ligne
			for i in range(1, self.empilement_par_moyenne.shape[0] - 1) :
				# Pour chaque colonne
				for j in range(1, self.empilement_par_moyenne.shape[1] - 1) :
					self.empilement_par_moyenne[i, j] = 255 - self.empilement_par_moyenne[i, j]
			# On rafraichit
			self.figure_images.add_subplot(2, 2, 2).clear()
			self.figure_images.add_subplot(2, 2, 2)
			# On affiche le graphique de la figure qui est le tableau numpy ndarray représentant l'image avec empilement par moyenne
			plt.imshow(self.empilement_par_moyenne)
			# L'axe x correspond à la longueur du tableau numpy ndarray
			plt.xlim(0, len(self.liste_ndarray[0][0]))
			# L'axe y correspond à la taille du tableau numpy ndarray divisé par sa longueur
			plt.ylim(0, self.liste_ndarray[0].size//len(self.liste_ndarray[0][0]))
			plt.colorbar(location="bottom")
			# On rafraichit
			self.canvas_images.draw()

  
	# Méthode connectée à un QPushButton qui permet de faire un reset
	def reset(self) :
		self.liste_ndarray = []
		self.empilement_par_somme = []
		self.empilement_par_mediane = []
		self.empilement_par_moyenne = []
		self.image_initiale = ""
		self.empilement = ""
		self.figure_images.clear()
		self.liste.clear()
		self.liste_informations.clear()
		self.label_chemin_fichier.setText("Chemin du dossier affiché à chaque nouvel empilement")
		self.canvas_images.draw()

  
# Programme principal	
  

if __name__ == "__main__" :
    
    appli = QApplication(sys.argv)
    fenetre = Fenetre()
    fenetre.show()
    sys.exit(appli.exec())