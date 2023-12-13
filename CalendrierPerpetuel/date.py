#%%
# Pap Alexandre
# BUT1 TPB
# SAE R101
# Implémentation des dates et calendriers
# Implémentation des tests (voir main en fin de fichier)

from typing import Dict, List, Tuple, NoReturn

import copy
import numpy as np

# ============================================================================= 
def format_affichage(affichage : str) : # Fonction qui vérifie si le format est français (fr) ou anglais (gb) en fonction de l'affichage entré en argument
    
    global format # La variable format devient globale
    
    if affichage == "fr" :
        format = "fr"
        
    elif affichage == "gb" :
        format = "gb"
        
    return


# =============================================================================
def cree_date(j: int, m: int, a: int) : # Fonction qui créé une date à partir de 3 entiers entrés en argument la décrivant
    """
    Crée une date à partir des entiers la décrivant.
    Si l'un des paramètres n'est pas un entier, la fonction retournera None

    >>> cree_date(15,12,2020)
    {'jour': 15, 'mois': 12, 'annee': 2020}
    >>> cree_date(1.5,12,2020)
    """
    global format # La variable format est globale car s'applique à toutes les fonctions et procédures
    
    dictionnaire_fr = {"jour" : j, "mois" : m, "annee" : a} # On définit la variable dictionnaire français au format de date j/m/a
    dictionnaire_gb = {"mois" : m, "jour" : j, "annee" : a} # On définit la variable dictionnaire anglais au format de date m/j/a
    reponse = {} # On définit la variable reponse qui affichera la date au format français ou anglais si les nombres entrés en argument sont bien entiers
    
    if ( type(dictionnaire_fr["jour"]) != int or type(dictionnaire_fr["mois"]) != int or type(dictionnaire_fr["annee"]) != int ) or ( type(dictionnaire_gb["mois"]) != int or type(dictionnaire_gb["jour"]) != int or type(dictionnaire_gb["annee"]) != int ) : # Si les nombres entrés en argument ne sont pas entiers, le format de date est nulle
        
        reponse = None
        
    else :
        
        # Format de date français ou anglais
        
        if format == "fr" :
            reponse = dictionnaire_fr
        elif format == "gb" :
            reponse = dictionnaire_gb
    
    return(reponse)


# =============================================================================
def est_bissextile(annee: int): # Fonction qui vérifie si l'année entrée en argument est bissextile ou non
    """
    retourne vrai si l'année est bissextile

    >>> est_bissextile(2020)
    True
    >>> est_bissextile(2021)
    False
    >>> est_bissextile(2022)
    False
    >>> est_bissextile(1900)
    False
    >>> est_bissextile(2000)
    True
    """ 
    reponse = False
    
    if annee % 4 == 0 : # Si le reste de la division de l'année par 4 vaut 0 l'année est divisible par 4
        if annee % 100 == 0 : # Si le reste de la division de l'année par 100 vaut 0 l'année est divisible par 4
            if annee % 400 == 0 : # Si le reste de la division de l'année par 400 vaut 0 l'année est divisible par 4
                reponse = True # Si l'année est divisible par 4, 100 et 400 l'année est bissextile
            else :
                reponse = False # Si l'année est divisible par 4, 100 mais pas 400 l'année n'est pas bissextile
        else :
            reponse = True # Si l'année est divisible par 4 mais pas par 100 et 400 l'année est bissextile
    else :
        reponse = False # Si l'année n'est pas divisible par 4 l'année n'est pas bissextile
    
    return(reponse)
    

# =============================================================================
def valide_simple(d: Dict): # Fonction qui vérifie si la date entrée en argument est valide ou non
    """   
    retourne vrai si la date est valide.
    on supposera que la date est valide si :
    - si le premier (le jour) est un entier compris entre 1 et 31
    - si le second (le mois) est un entier compris entre 1 et 12

    >>> date = cree_date(1, 2, 0)
    >>> valide_simple(date)
    True
    >>> date = cree_date(1.5, 5, 6)
    >>> valide_simple(date)
    False
    >>> date = cree_date(0, 5, 6)
    >>> valide_simple(date)
    False
    >>> date = cree_date(20, 8, 2021)
    >>> valide_simple(date)
    True
    """
    global format # La variable format est globale car s'applique à toutes les fonctions et procédures
    
    reponse = False
    d_values = {} # On définit la variable dictionnaire d_values qui récupère les valeurs de dictionnaire
    d_list = [] # On définit la variable liste d_list qui récupère les valeurs de d_values sous forme de liste
    
    if d == None : # Si la date entrée n'est pas au bon format, la valide simple est incorrecte
        reponse = False
    
    elif d != None :
        
        d_values = d.values() # Récupération des valeurs de la date entrée en dictionnaire
        d_list = list(d_values) # Récupération des valeurs précédentes sous forme de liste
    
        # Si la date entrée est au bon format et respecte les conditions basiques de mois et de jours, la valide simple est correcte, sinon elle est fausse
    
        if ( 1 <= d_list[0] <= 31 and 1 <= d_list[1] <= 12 and format == "fr") or ( 1 <= d_list[1] <= 31 and 1 <= d_list[0] <= 12 and format == "gb") :
            reponse = True
        else :
            reponse = False
        
    return(reponse)
    

# =============================================================================
def valide_complet(d: Dict): # Fonction qui vérifie si la date entrée en argument est totalement valide ou non
    """ 
    retourne vrai si la date est valide.
    on supposera que la date est valide si :
    - la validation simple est vraie
    - si la date représente une date réelle 

    >>> date = cree_date(15, 1, 2022)
    >>> valide_complet(date)
    True
    >>> date = cree_date(32, 1, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(-1, 1, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(31, 6, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(29, 2, 2020)
    >>> valide_complet(date)
    True
    >>> date = cree_date(29, 2, 2022)
    >>> valide_complet(date)
    False
    """
    global format # La variable format est globale car s'applique à toutes les fonctions et procédures
    
    reponse = False
    d_values = {} # On définit la variable dictionnaire d_values qui récupère les valeurs de dictionnaire
    d_list = [] # On définit la variable liste d_list qui récupère les valeurs de d_values sous forme de liste
    
    if d == None : # Si la date entrée n'est pas au bon format, la valide complète est incorrecte
        reponse = None
    
    elif d != None and valide_simple(d) == True : # Si la date entrée est au bon format et respecte la valide simple, on vérifie en fonction des mois et des années bissextiles ou non
        
        d_values = d.values() # Récupération des valeurs de la date entrée en dictionnaire
        d_list = list(d_values) # Récupération des valeurs précédentes sous forme de liste
    
        if ( d_list[2] > 0 and type(d_list[2]) == int ) : # Si l'année de la date est entière et positive on continue
            
            # Vérification pour les mois de 30 jours au format français et anglais
            
            if ( 1 <= d_list[0] <= 30 and d_list[1] != 2 and ( d_list[1] == 4 or d_list[1] == 6 or d_list[1] == 9 or d_list[1] == 11 ) and format == "fr" ) or ( 1 <= d_list[1] <= 30 and d_list[0] != 2 and ( d_list[0] == 4 or d_list[0] == 6 or d_list[0] == 9 or d_list[0] == 11 ) and format == "gb" ) :
                
                reponse = True
        
            # Vérificiation pour les mois de 29 jours : Février en année bissextile
        
            elif ( est_bissextile(d_list[2]) == True and d_list[1] == 2 and 1 <= d_list[0] <= 29 and format == "fr" ) or ( est_bissextile(d_list[2]) == True and d_list[0] == 2 and 1 <= d_list[1] <= 29 and format == "gb" ) :
            
                reponse = True

            # Vérification pour les mois de 28 jours : Février en année non-bissextile
            
            elif ( est_bissextile(d_list[2]) == False and d_list[1] == 2 and 1 <= d_list[0] <= 28 and format == "fr" ) or ( est_bissextile(d_list[2]) == False and d_list[0] == 2 and 1 <= d_list[1] <= 28 and format == "gb" ) :
            
                reponse = True
            
            # Vérification pour les mois de 31 jours au format français et anglais
            
            elif ( 1 <= d_list[1] <= 31 and ( d_list[1] == 1 or d_list[1] == 3 or d_list[1] == 5 or d_list[1] == 7 or d_list[1] == 8 or d_list[1] == 10 or d_list[1] == 12 ) and format == "fr" ) or ( 1 <= d_list[0] <= 31 and ( d_list[0] == 1 or d_list[0] == 3 or d_list[0] == 5 or d_list[0] == 7 or d_list[0] == 8 or d_list[0] == 10 or d_list[0] == 12 ) and format == "gb" ) :
                
                reponse = True
        
        else :
        
            reponse = False
    
    return(reponse)


# =============================================================================
def compare(d1: Dict, d2: Dict): # Fonction qui vérifie si les comparaisons entre deux dates sont correctes ou non indépendamment des formats fr et gb
    """
    Permet de classer deux dates.
    Retourne
    -1 si la date d1 < d2
    +1 si la date d1 > d2
    0 si les dates sont identiques
    on considère que les dates sont croissantes 
    dans l'ordre chronologique

    >>> date1 = cree_date(25,12,2021)
    >>> date2 = cree_date(31,12,2021)
    >>> compare(date1,date2)
    -1
    >>> compare(date2,date1)
    1
    >>> compare(date1,date1)
    0
    """
    reponse = 0
    d1_values = {} # On définit la variable dictionnaire d1_values qui récupère les valeurs de dictionnaire
    d2_values = {} # On définit la variable dictionnaire d2_values qui récupère les valeurs de dictionnaire
    d1_list = [] # On définit la variable liste d1_list qui récupère les valeurs de d1_values sous forme de liste
    d2_list = [] # On définit la variable liste d2_list qui récupère les valeurs de d2_values sous forme de liste
    
    if d1 == None and d2 == None : # Si la date entrée n'est pas au bon format, la comparaison est incorrecte
        reponse = None
    
    if d1 != None and d2 != None :
    
        d1_values = d1.values() # Récupération des valeurs de d1 entrée en dictionnaire
        d2_values = d2.values() # Récupération des valeurs de d2 en dictionnaire
        d1_list = list(d1_values) # Récupération des valeurs précédentes d1 sous forme de liste
        d2_list = list(d2_values) # Récupération des valeurs précédentes d2 sous forme de liste
    
        # Cas où d1 < d2 :
    
        if ( d1_list[0] < d2_list[0] ) or ( d1_list[1] < d2_list[1] ) or ( d1_list[2] < d2_list[2] ) :
            reponse = -1
            
        # Cas où d1 > d2 :
        
        elif ( d1_list[0] > d2_list[0] ) or ( d1_list[1] > d2_list[1] ) or ( d1_list[2] > d2_list[2] ) :
            reponse = +1
            
        # Cas où d1 = d2 :
        
        elif ( d1_list[0] == d2_list[0] ) and ( d1_list[1] == d2_list[1] ) and ( d1_list[2] == d2_list[2] ) :
            reponse = 0
    
    return(reponse)    


# ============================================================================= 
def calcule_jour(date : Dict): # Fonction qui retourne le jour d'un mois d'une année en jour de la semaine d'un mois d'une année

    global format # La variable format est globale car s'applique à toutes les fonctions et procédures

    jour = 0
    date_values = {} # On définit la variable dictionnaire date_values qui récupère les valeurs de dictionnaire
    date_keys = {} # On définit la variable dictionnaire date_keys qui récupère les clés de dictionnaire
    date_values_list = [] # On définit la variable liste date_values_list qui récupère les valeurs de date_values sous forme de liste
    date_keys_list = [] # On définit la variable liste date_keys_list qui récupère les valeurs de date_keys sous forme de liste

    if date == None : # Si la date entrée n'est pas au bon format, le calcul est incorrect
        date = None

    elif date != None and valide_complet(date) == True : # Si la date entrée est au bon format, on vérifie si la validation complète est correcte et on continue
    
        date_values = date.values() # Récupération des valeurs de date_values entrée en dictionnaire
        date_keys = date.keys() # Récupération des valeurs de date_keys entrée en dictionnaire
        date_values_list = list(date_values) # Récupération des valeurs précédentes date_values sous forme de liste
        date_keys_list = list(date_keys) # Récupération des valeurs précédentes date_keys sous forme de liste

        # Algorithme de Mike Keith

        if format == "fr" :

            if date_values_list[1] < 3 :
                
                jour = ( int( (23*date_values_list[1])/9 ) + date_values_list[0] + 4 + date_values_list[2] + int( (date_values_list[2]-1)/4 ) - int( (date_values_list[2]-1)/100 ) + int( (date_values_list[2]-1)/400 ) ) % 7

            elif date_values_list[1] > 3 :
                
                jour = ( int( (23*date_values_list[1])/9 ) + date_values_list[0] + 2 + date_values_list[2] + int( (date_values_list[2])/4 ) - int( (date_values_list[2])/100 ) + int( (date_values_list[2])/400 ) ) % 7

            if jour == 0 :
                date_values_list[0] = "Dim" 
            elif jour == 1 :
                date_values_list[0] = "Lun"
            elif jour == 2 :
                date_values_list[0] = "Mar" 
            elif jour == 3 :
                date_values_list[0] = "Mer" 
            elif jour == 4 :
                date_values_list[0] = "Jeu" 
            elif jour == 5 :
                date_values_list[0] = "Ven"
            elif jour == 6 :
                date_values_list[0] = "Sam" 
                
            # Modification de la date au format jour semaine / mois / anneee
            
            date = {date_keys_list[0] : date_values_list[0], date_keys_list[1] : date_values_list[1], date_keys_list[2] :date_values_list[2]}

        # Algorithme de Mike Keith

        elif format == "gb" :
    
            if date_values_list[0] < 3 :
                
                jour = ( int( (23*date_values_list[0])/9 ) + date_values_list[1] + 4 + date_values_list[2] + int( (date_values_list[2]-1)/4 ) - int( (date_values_list[2]-1)/100 ) + int( (date_values_list[2]-1)/400 ) ) % 7

            elif date_values_list[0] > 3 :
                
                jour = ( int( (23*date_values_list[0])/9 ) + date_values_list[1] + 2 + date_values_list[2] + int( (date_values_list[2])/4 ) - int( (date_values_list[2])/100 ) + int( (date_values_list[2])/400 ) ) % 7

            if jour == 0 :
                date_values_list[1] = "Dim" 
            elif jour == 1 :
                date_values_list[1] = "Lun"
            elif jour == 2 :
                date_values_list[1] = "Mar" 
            elif jour == 3 :
                date_values_list[1] = "Mer" 
            elif jour == 4 :
                date_values_list[1] = "Jeu" 
            elif jour == 5 :
                date_values_list[1] = "Ven"
            elif jour == 6 :
                date_values_list[1] = "Sam" 

            # Modification de la date au format mois / jour semaine / anneee

            date = {date_keys_list[0] : date_values_list[0], date_keys_list[1] : date_values_list[1], date_keys_list[2] :date_values_list[2]}

    return(date)


# ============================================================================= 
def modif_date(date : Dict, n : int): # Fonction qui retourne une date ajoutée n fois ou retranchée n fois à partir de la date initiale
    
    global format # La variable format est globale car s'applique à toutes les fonctions et procédures
    
    date_values = {} # On définit la variable dictionnaire date_values qui récupère les valeurs de dictionnaire
    date_keys = {} # On définit la variable dictionnaire date_keys qui récupère les clés de dictionnaire
    date_values_list = [] # Récupération des valeurs précédentes date_values sous forme de liste
    date_keys_list = [] # Récupération des valeurs précédentes date_keys sous forme de liste
    compteur_mois = 0 # Le compteur du mois correspond au mois de la date ajoutée ou retranchée
    
    liste_mois_en_jour = [] # On définit une liste contenant 28 29 30 et 31 jours suivant les mois et les années bissextiles ou non
    equivalent_mois_jours = 0 # L'équivalent_mois_jours correspond au nombre de jour dans chaque mois suivant (ajouter) ou précédant (retrancher) la date initiale
    jour_initial = 0 # Le jour initial correspond 
    changement_gb = 0 # On définit une variable chargée d'adapter au format britannique mois / jour / annee
    
    if date == None : # Si la date n'est pas au bon format, la date retournée sera nulle
        date = None
    
    elif date != None and valide_complet(date) == True : # Si la date est au bon format, on continue
        
        if format == "fr" :
            changement_gb = 0 # Format français : il n'y a pas de changement
        elif format == "gb" :
            changement_gb = 1 # Format britannique : il y a le changement de format mois / annee
        
        date_values = date.values() # Récupération des valeurs de date_values en dictionnaire
        date_keys = date.keys() # Récupération des clés de date_keys en dictionnaire
        date_values_list = list(date_values) # Récupération des valeurs de date_values en liste
        date_keys_list = list(date_keys) # Récupération des valeurs de date_keys en liste
        compteur_mois = date_values_list[1 - changement_gb] # On change le compteur ou non suivant le format fr ou gb (jour / mois ou mois / jour)
        
        liste_mois_en_jour = [28, 29, 30, 31] # La liste du nombre de jours des différents mois
        
        if date_values_list[1 - changement_gb] == 2 and est_bissextile(date_values_list[2]) == False :
            equivalent_mois_jours = liste_mois_en_jour[0] # L'équivalent jour mois est 28 si Février année non bissextile
        elif date_values_list[1 - changement_gb] == 2 and est_bissextile(date_values_list[2]) == True :
            equivalent_mois_jours = liste_mois_en_jour[1] # L'équivalent jour mois est 29 si Février année bissextile
        elif ( compteur_mois == 4 or compteur_mois == 6 or compteur_mois == 9 or compteur_mois == 11 ) and date_values_list[1 - changement_gb] != 2 :
            equivalent_mois_jours = liste_mois_en_jour[2] # L'équivalent jour mois est 30 hors Février
        elif ( compteur_mois == 1 or compteur_mois == 3 or compteur_mois == 5 or compteur_mois == 7 or compteur_mois == 8 or compteur_mois == 10 or compteur_mois == 12 ) and date_values_list[1 - changement_gb] != 2 :
            equivalent_mois_jours = liste_mois_en_jour[3] # L'équivalent jour mois est 31 hors Février
        
        if n > 0 and equivalent_mois_jours != 0 : # Ajouter n entier à une date : on retranche ce que l'on va ajouter pour le mettre sous forme de date
            
            date_values_list[0 + changement_gb] = date_values_list[0 + changement_gb] + n # On ajoute n au jour de la date
            
            while (1 <= date_values_list[0 + changement_gb] <= equivalent_mois_jours) == False : # Tant que la date finale n'est pas comprise dans un bon intervalle, la boucle continue
                
                date_values_list[0 + changement_gb] = date_values_list[0 + changement_gb] - equivalent_mois_jours # On retranche ce que l'on va ajouter pour le mettre sous forme de date comprise entre 1 et le mois suivant (ajout) 
                compteur_mois = compteur_mois + 1 # Le mois suivant, on ajoute 1 au mois initial
                date_values_list[1 - changement_gb] = compteur_mois # On change le mois suivant le format fr ou gb suite à l'ajout de 1 au mois initial
                
                if ( compteur_mois == 4 or compteur_mois == 6 or compteur_mois == 9 or compteur_mois == 11 ) :
                    equivalent_mois_jours = 30 # L'équivalent jour mois est 30 hors Février avec le mois suivant
                elif ( compteur_mois == 1 or compteur_mois == 3 or compteur_mois == 5 or compteur_mois == 7 or compteur_mois == 8 or compteur_mois == 10 or compteur_mois == 12 ) :
                    equivalent_mois_jours = 31 # L'équivalent jour mois est 31 hors Février avec le mois suivant
                elif compteur_mois == 2 and est_bissextile(date_values_list[2]) == True :
                    equivalent_mois_jours = 29 # L'équivalent jour mois est 29 si Février année bissextile avec le mois suivant
                elif compteur_mois == 2 and est_bissextile(date_values_list[2]) == False :
                    equivalent_mois_jours = 28 # L'équivalent jour mois est 28 si Février année non bissextile avec le mois suivant
                if compteur_mois > 12 : # Si le mois suivant est supérieur à 12
                    compteur_mois = 1 # Le mois suivant est réinitialisé à 1 (Janvier)
                    date_values_list[1 - changement_gb] = 1 # On change le mois suivant le format fr ou gb suite à la réinitialisation
                    date_values_list[2] = date_values_list[2] + 1 # On a réinitialisé le mois, donc on est à l'année suivante

            # Modification de la date initiale au format fr ou gb : on la remplace par la date ajoutée n fois à la date initiale

            date = {date_keys_list[0] : date_values_list[0], date_keys_list[1] : date_values_list[1], date_keys_list[2] : date_values_list[2]}
            
        elif n < 0 and equivalent_mois_jours != 0 : # Retrancher n entier à une date : on ajoute ce que l'on va retrancher pour le mettre sous forme de date
            
            jour_initial = copy.copy(date_values_list[0 + changement_gb]) # On copie la valeur du jour de la date initiale au format fr ou gb
            date_values_list[0 + changement_gb] = date_values_list[0 + changement_gb] + n # On retranche n au jour de la date
            
            while (1 <= date_values_list[0 + changement_gb] <= equivalent_mois_jours) == False : # Tant que la date finale n'est pas comprise dans un bon intervalle, la boucle continue
                
                date_values_list[0 + changement_gb] = date_values_list[0 + changement_gb] + equivalent_mois_jours # On ajoute ce que l'on va retrancher pour le mettre sous forme de date comprise entre 1 et le mois précédant (retrancher) 
                compteur_mois = compteur_mois - 1 # Le mois suivant, on retranche 1 au mois initial
                date_values_list[1 - changement_gb] = compteur_mois # On change le mois suivant le format fr ou gb suite à 1 que l'on a retranché au mois initial
                
                if ( compteur_mois == 4 or compteur_mois == 6 or compteur_mois == 9 or compteur_mois == 11 ) :
                    equivalent_mois_jours = 30 # L'équivalent jour mois est 30 hors Février avec le mois précédant
                elif ( compteur_mois == 1 or compteur_mois == 3 or compteur_mois == 5 or compteur_mois == 7 or compteur_mois == 8 or compteur_mois == 10 or compteur_mois == 12 ) :
                    equivalent_mois_jours = 31 # L'équivalent jour mois est 30 hors Février avec le mois précédant
                elif compteur_mois == 2 and est_bissextile(date_values_list[2]) == True :
                    equivalent_mois_jours = 29 # L'équivalent jour mois est 29 si Février année bissextile avec le mois précédant
                elif compteur_mois == 2 and est_bissextile(date_values_list[2]) == False :
                    equivalent_mois_jours = 28 # L'équivalent jour mois est 28 si Février année bissextile avec le mois précédant
                if compteur_mois < 1 : # Si le mois précédant est inférieur à 1
                    compteur_mois = 12 # Le mois précédant est réinitialisé à 12 (Décembre)
                    date_values_list[1 - changement_gb] = 12 # On change le mois suivant le format fr ou gb suite à la réinitialisation
                    date_values_list[2] = date_values_list[2] - 1 # On a réinitialisé le mois, donc on est à l'année précédante
            
            if jour_initial + n <= 0 : # Si la différence du jour initiale et de n retranchée est négative on ajoute 1 suite au décalage entre le jour 1 et le jour précédant (28, 29, 30, 31)
                date_values_list[0 + changement_gb] = date_values_list[0 + changement_gb] + 1
            
            # Modification de la date initiale au format fr ou gb : on la remplace par la date retranchée n fois à la date initiale
            
            date = {date_keys_list[0] : date_values_list[0], date_keys_list[1] : date_values_list[1], date_keys_list[2] : date_values_list[2]}

    return(date)


# ============================================================================= 
def calcule_veille_lendemain(date : Dict): # Fonction qui retourne la date de la veille et du lendemain en fonction de la date entrée en argument

    date_veille = {}
    date_lendemain = {}

    if date == None : # Si la date n'est pas au bon format, la date de la veille et du lendemain ne seront pas au bon format
        date_veille = None
        date_lendemain = None

    elif date != None : # Sinon on utilise la fonction modif_date en retranchant 1 et en ajoutant 1 à la date

        date_veille = modif_date(date, -1)
        date_lendemain = modif_date(date, 1)
    
    return(date_veille, date_lendemain)


# ============================================================================= 
def ajoute_n_jour(date : Dict, n : int): # Fonction qui ajoute n jour à la date entrée en argument

    if date == None :  # Si la date n'est pas au bon format
        date = None

    elif date != None : # Sinon on utilise la fonction modif_date en ajoutant 1 à la date initiale si n est positif
        
        if n > 0 :
            date = modif_date(date, n)
    
    return(date)


# ============================================================================= 
def retranche_n_jour(date : Dict, n : int): # Fonction qui retranche n jour à la date entrée en argument

    if date == None : # Si la date n'est pas au bon format
        date = None

    elif date != None : # Sinon on utilise la fonction modif_date en retranchant 1 à la date initiale si n est négatif

        if n < 0 :
            date = modif_date(date, n)
    
    return(date)


# ============================================================================= 
def ecart_jour(date1 : Dict, date2 : Dict): # Fonction qui retourne l'écart entre deux dates entrées en argument

    i = 1

    if date1 == None or date2 == None : # Si la date n'est pas au bon format
        i = None
    
    elif date1 != None and date2 != None : # Sinon
        
        if compare(date1, date2) == - 1 : # Si d1 < d2 alors :
        
            while modif_date(date1, i) != date2 : # On ajoute i fois (écart) 1 à d1 jusqu'à ce qu'elle soit égale à d2
                i = i + 1
    
        elif compare(date1, date2) == + 1 : # Si d1 > d2 alors :
        
            while modif_date(date1, i) != date2 : # On retranche i fois (écart) 1 à d1 jusqu'à ce qu'elle soit égale à d2
                i = i - 1
    
    return(abs(i))


# =============================================================================
def copie_date(date: Dict): # Fonction qui copie une date
    """
    copie la date passée en paramètre
    """
    copie_date = {}
    
    if date == None : # Si la date n'est pas au bon format
        copie_date = None
    
    elif date != None : # Sinon on utilise la méthode copy() pour copier la date
        copie_date = copy.copy(date)
    
    return(copie_date)


# =============================================================================
def ajoute_calendrier(calendrier: List, date: Dict, description: str ): # Fonction qui ajoute une date et sa description au calendrier
    """
    ajoute un élément à la liste du calendrier.
    """
    global format # La variable format est globale car s'applique à toutes les fonctions et procédures
    
    if date != None and valide_complet(date) == True and format == "fr" :
        calendrier.append(date)
        calendrier.append(description)
    
    elif date != None and valide_complet(date) == True and format == "gb" :
        calendrier.append(date)
        calendrier.append(description)
    
    return


# =============================================================================
def ajoute_fetes(calendrier : List, annee : int): # Fonction qui ajoute les fêtes avec les dates et descriptions au calendrier suivant le format fr ou gb
    
    global format # La variable format est globale car s'applique à toutes les fonctions et procédures
    
    if format == "fr" :
    
        ajoute_calendrier(calendrier, cree_date(1, 1, annee), "Jour de l'an")
        ajoute_calendrier(calendrier, cree_date(1, 5, annee), "Fête du travail")
        ajoute_calendrier(calendrier, cree_date(8, 5, annee), "Armistice 1945")
        ajoute_calendrier(calendrier, cree_date(14, 7, annee), "Fête nationale")
        ajoute_calendrier(calendrier, cree_date(15, 8, annee), "Assomption")
        ajoute_calendrier(calendrier, cree_date(25, 12, annee), "Noël")
        ajoute_calendrier(calendrier, cree_date(10, 12, annee), "Date sortie de Doom")
    
    elif format == "gb" :
        
        ajoute_calendrier(calendrier, cree_date(1, 1, annee), "Jour de l'an")
        ajoute_calendrier(calendrier, cree_date(5, 1, annee), "Fête du travail")
        ajoute_calendrier(calendrier, cree_date(5, 8, annee), "Armistice 1945")
        ajoute_calendrier(calendrier, cree_date(7, 14, annee), "Fête nationale")
        ajoute_calendrier(calendrier, cree_date(8, 15, annee), "Assomption")
        ajoute_calendrier(calendrier, cree_date(12, 25, annee), "Noël")
        ajoute_calendrier(calendrier, cree_date(12, 10, annee), "Date sortie de Doom")
    
    return


# =============================================================================
def trouve_evenement(calendrier : List, date : Dict): # Fonction qui vérifie si la date entrée en argument correspond à la date d'un évènement
    
    global format # La variable format est globale car s'applique à toutes les fonctions et procédures
    
    reponse = ""
    date_values = {}
    date_list = []
    
    if date == None : # Si la date n'est pas au bon format
        reponse == None
    
    elif date != None : # Sinon
        
        if valide_complet(date) == True :
        
            date_values = date.values()
            date_list = list(date_values)
        
            if ( date_list[0] == 1 and date_list[1] == 1 and format == "fr" ) or ( date_list[0] == 1 and date_list[1] == 1 and format == "gb" ) :
                reponse = "Jour de l'an"
            elif ( date_list[0] == 1 and date_list[1] == 5 and format == "fr" ) or ( date_list[0] == 5 and date_list[1] == 1 and format == "gb" ) :
                reponse = "Fête du travail"
            elif ( date_list[0] == 8 and date_list[1] == 5 and format == "fr" ) or ( date_list[0] == 5 and date_list[1] == 8 and format == "gb" ) :
                reponse = "Armistice 1945"
            elif ( date_list[0] == 14 and date_list[1] == 7 and format == "fr" ) or ( date_list[0] == 7 and date_list[1] == 14 and format == "gb" ) :
                reponse = "Fête nationale"
            elif ( date_list[0] == 15 and date_list[1] == 8 and format == "fr" ) or ( date_list[0] == 8 and date_list[1] == 15 and format == "gb" ) :
                reponse = "Assomption"
            elif ( date_list[0] == 25 and date_list[1] == 12 and format == "fr" ) or ( date_list[0] == 12 and date_list[1] == 25 and format == "gb" ) :
                reponse = "Noël"
            elif ( date_list[0] == 10 and date_list[1] == 12 and format == "fr" ) or ( date_list[0] == 12 and date_list[1] == 10 and format == "gb" ) :
                reponse = "Date sortie de Doom"
    
    return(reponse)


# =============================================================================
def affiche_calendrier(calendrier: List, annee : int): # Procédure qui affiche les évènements ajoutés au calendrier
    """
    affiche le calendrier sous forme de liste.
    """
    ajoute_fetes(calendrier, annee)

    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    print(" Evènements : ")
    
    for i in range(0, len(calendrier) - 1) :
        if type(calendrier[i]) == dict :
            calendrier_values_i = calendrier[i].values()
            calendrier_list_i = list(calendrier_values_i)
            print("Le", calendrier_list_i[0], "/", calendrier_list_i[1], "/", calendrier_list_i[2], ":", calendrier[i + 1])
    
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")


# ============================================================================= 

def afficheur_mensuel_tableau(calendrier : List, mois : int, annee : int): # Procédure qui affiche le calendrier mensuel sous forme de tableau

    date = cree_date(1, mois, annee)
    
    date29 = modif_date(date, 28)
    date30 = modif_date(date, 29)
    date31 = modif_date(date, 30)

    if modif_date(date, 28)["mois"] != mois :
        date29 = ""
    elif modif_date(date, 29)["mois"] != mois :
        date30 = ""
    elif modif_date(date, 30)["mois"] != mois :
        date31 = ""
    
    if mois == 1 :
        mois = "Janvier  "
    elif mois == 2 :
        mois = "Février  "
    elif mois == 3 :
        mois = "Mars     "
    elif mois == 4 :
        mois = "Avril    "
    elif mois == 5 :
        mois = "Mai      "
    elif mois == 6 :
        mois = "Juin     "
    elif mois == 7 :
        mois = "Juillet  "
    elif mois == 8 :
        mois = "Août     "
    elif mois == 9 :
        mois = "Septembre"
    elif mois == 10 :
        mois = "Octobre  "
    elif mois == 11 :
        mois = "Novembre "
    elif mois == 12 :
        mois = "Décembre "
    
    print("-----------------------------------------------------------------------------------------------")
    print("                     *    *    *  *    ",mois,"",annee,"    *  *    *    *                     ")
    print("-----------------------------------------------------------------------------------------------")
    print(calcule_jour(date)["jour"]," ",date["jour"]," | ",calcule_jour(modif_date(date,1))["jour"]," ",modif_date(date,1)["jour"]," | ",calcule_jour(modif_date(date,2))["jour"]," ",modif_date(date,2)["jour"]," | ",calcule_jour(modif_date(date,3))["jour"]," ",modif_date(date,3)["jour"]," | ",calcule_jour(modif_date(date,4))["jour"]," ",modif_date(date,4)["jour"]," | ",calcule_jour(modif_date(date,5))["jour"]," ",modif_date(date,5)["jour"]," | ",calcule_jour(modif_date(date,6))["jour"]," ",modif_date(date,6)["jour"]," | ")
    print("-----------------------------------------------------------------------------------------------")
    print(calcule_jour(modif_date(date,7))["jour"]," ",modif_date(date,7)["jour"]," | ",calcule_jour(modif_date(date,8))["jour"]," ",modif_date(date,8)["jour"]," | ",calcule_jour(modif_date(date,9))["jour"]," ",modif_date(date,9)["jour"]," | ",calcule_jour(modif_date(date,10))["jour"]," ",modif_date(date,10)["jour"]," | ",calcule_jour(modif_date(date,11))["jour"]," ",modif_date(date,11)["jour"]," | ",calcule_jour(modif_date(date,12))["jour"]," ",modif_date(date,12)["jour"]," | ",calcule_jour(modif_date(date,13))["jour"]," ",modif_date(date,13)["jour"]," | ")
    print("-----------------------------------------------------------------------------------------------")
    print(calcule_jour(modif_date(date,14))["jour"]," ",modif_date(date,14)["jour"]," | ",calcule_jour(modif_date(date,15))["jour"]," ",modif_date(date,15)["jour"]," | ",calcule_jour(modif_date(date,16))["jour"]," ",modif_date(date,16)["jour"]," | ",calcule_jour(modif_date(date,17))["jour"]," ",modif_date(date,17)["jour"]," | ",calcule_jour(modif_date(date,18))["jour"]," ",modif_date(date,18)["jour"]," | ",calcule_jour(modif_date(date,19))["jour"]," ",modif_date(date,19)["jour"]," | ",calcule_jour(modif_date(date,20))["jour"]," ",modif_date(date,20)["jour"]," | ")
    print("-----------------------------------------------------------------------------------------------")
    print(calcule_jour(modif_date(date,21))["jour"]," ",modif_date(date,21)["jour"]," | ",calcule_jour(modif_date(date,22))["jour"]," ",modif_date(date,22)["jour"]," | ",calcule_jour(modif_date(date,23))["jour"]," ",modif_date(date,23)["jour"]," | ",calcule_jour(modif_date(date,24))["jour"]," ",modif_date(date,24)["jour"]," | ",calcule_jour(modif_date(date,25))["jour"]," ",modif_date(date,25)["jour"]," | ",calcule_jour(modif_date(date,26))["jour"]," ",modif_date(date,26)["jour"]," | ",calcule_jour(modif_date(date,27))["jour"]," ",modif_date(date,27)["jour"]," | ")
    print("-----------------------------------------------------------------------------------------------")
    print(calcule_jour(date29)["jour"]," ",date29["jour"]," | ",calcule_jour(date30)["jour"]," ",date30["jour"]," | ",calcule_jour(date31)["jour"]," ",date31["jour"]," | ")
    print("-----------------------------------------------------------------------------------------------")       


# ============================================================================= 

if __name__ == '__main__':
    
    format = str(input("Entrez fr ou gb (format date) : "))
    mois = int(input("Entrez un mois (entre 1 et 12) : "))
    annee = int(input("Entrez une année : "))
    
    calendrier = []
    afficheur_mensuel_tableau(calendrier, mois, annee)
    affiche_calendrier(calendrier, annee)

# %%
