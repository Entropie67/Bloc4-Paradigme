#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from classes import *
from constantes import *
import random

def fin(x, y):
	"""
	Fonction qui vérifie si c'est gagé
	:param x: position x du personnage
	:param y: position y du personnage
	:return: True si c'est perdu, False si c'est gagné
	"""
	if niveau.structure[x][y] == 'a':
		if loli.compteur == 3:
			fenetre.blit(victoire, (50, 50))
		else:
			fenetre.blit(defaite, (50, 50))
		pygame.display.flip()
		pygame.time.delay(5000)
		return False
	else:
		return True

pygame.init()
#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone
icone = pygame.image.load(IMAGES_PERSONNAGE[0][0])
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)

#BOUCLE PRINCIPALE
continuer = 1
while continuer:	
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))
	#Rafraichissement
	pygame.display.flip()
	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu, continuer_accueil = 1, 1
	#BOUCLE D'ACCUEIL
	while continuer_accueil:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable de choix du niveau
				choix = 0
				
			elif event.type == KEYDOWN:				
				#Lancement du niveau 1
				if event.key == K_RETURN:
					continuer_accueil = 0	#On quitte l'accueil
					choix = 1
			

	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load(image_fond).convert()

		#Génération d'un niveau à partir d'un fichier
		niveau = Niveau(random.choice(LEVEL))
		niveau.afficher(fenetre)

		#Création de Macgyver
		loli = Perso(niveau)
		victoire = pygame.image.load(IMAGE_VICTOIRE).convert_alpha()
		defaite = pygame.image.load(IMAGE_DEFAITE).convert_alpha()
		#placement des items
		tube = Item(image_tube, niveau)
		seringue = Item(image_seringue, niveau)
		ether = Item(image_ether, niveau)

	#BOUCLE DE JEU
	while continuer_jeu:
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
		for event in pygame.event.get():
			#Si l'utilisateur quitte, on met la variable qui continue le jeu
			#ET la variable générale à 0 pour fermer la fenêtre
			if event.type == QUIT:
				continuer_jeu = 0
				continuer = 0
			elif event.type == KEYDOWN:
				#Si l'utilisateur presse Echap ici, on revient seulement au menu
				if event.key == K_ESCAPE:
					continuer_jeu = 0
				#Touches de déplacement de Macgyver
				elif event.key == K_RIGHT:
					loli.deplacer('droite')
				elif event.key == K_LEFT:
					loli.deplacer('gauche')
				elif event.key == K_UP:
					loli.deplacer('haut')
				elif event.key == K_DOWN:
					loli.deplacer('bas')
			
		#Affichages aux nouvelles positions
		fenetre.blit(fond, (0,0))
		niveau.afficher(fenetre)
		fenetre.blit(loli.image, (loli.x, loli.y)) #loli.direction = l'image dans la bonne direction
		if(niveau.structure[tube.case_y][tube.case_x] == 'i'):
			fenetre.blit(tube.image, (tube.x, tube.y))
		if(niveau.structure[seringue.case_y][seringue.case_x] == 'i'):
			fenetre.blit(seringue.image, (seringue.x, seringue.y))
		if (niveau.structure[ether.case_y][ether.case_x] == 'i'):
			fenetre.blit(ether.image, (ether.x, ether.y))
		pygame.display.flip()
		continuer_jeu = fin(loli.case_y, loli.case_x)




