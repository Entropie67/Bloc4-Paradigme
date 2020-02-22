"""Constantes du jeu de Labyrinthe Macgyver"""

# Paramètres de la fenêtre
nombre_sprite_cote = 15
taille_sprite = 30
cote_fenetre = nombre_sprite_cote * taille_sprite

# Personnalisation de la fenêtre
titre_fenetre = "Jeu de Labyrinthe"

################################################################
# Images
PATH = "images/"
FORMAT = ".png"
DIRECTIONS = ("droite", "bas", "gauche", "haut")
IMAGES_PERSONNAGE = [[PATH+i+str(j)+FORMAT for j in range(1, 4)] for i in DIRECTIONS]

################################################################
# Listes des images du jeu
image_accueil = "images/accueil.png"
image_fond = "images/fond.jpg"
image_mur = "images/mur.png"
image_depart = "images/depart.png"
image_arrivee = "images/arrivee.png"
image_seringue = "images/seringue.png"
image_tube = "images/tube_plastique.png"
image_ether = "images/ether.png"

