#!/usr/bin/python3
# -*- coding: Utf-8 -*
import pygame
from pygame.locals import *
from random import *

nombre_sprite_cote = 15
taille_sprite = 30
cote_fenetre = nombre_sprite_cote * taille_sprite
titre_fenetre = "Jeu de labyrinthe"
image_icone = "images/mg_droite.png"
image_accueil = "images/accueil.png"
image_fond = "images/fond.jpg"
image_mur = "images/mur.png"
image_depart = "images/depart.png"
image_arrivee = "images/arrivee.png"
image_seringue = "images/seringue.png"
image_tube = "images/tube_plastique.png"
image_ether = "images/ether.png"

with open('n1', "r") as fichier:
        structure_niveau = []		
        for ligne in fichier:
                ligne_niveau = []
                for sprite in ligne:
                        if sprite != '\n':
                                ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)
        structure = structure_niveau

class Perso:
	def __init__(self, image, structure):
		#Sprites du personnage
		self.image = pygame.image.load(image).convert_alpha()
				#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.image
		#Niveau dans lequel le personnage se trouve 
		self.structure = structure
		self.compteur = 0

	def deplacer(self, direction):
		if (self.structure[self.case_y][self.case_x] == 'i'):
			self.compteur += 1
			print(self.compteur)
			self.structure[self.case_y][self.case_x] = '0'
		#Déplacement vers la droite
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.structure[self.case_y][self.case_x+1] != 'm':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			#Image dans la bonne direction
			self.direction = self.image
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.image
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.image
		
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.image


class Item:
	def __init__(self, image, structure):
		# Sprites de l'objet
		self.image = pygame.image.load(image).convert_alpha()
		# Niveau dans lequel l'objet se trouve
		self.structure = structure
		self.case_x = 0
		self.case_y = 0

		continuerob = True
		while continuerob:
			x = randint(0,14)
			y = randint(0,14)
			if self.structure[y][x] == '0':
				continuerob = False
				self.structure[y][x] = 'i'
			else:
				continuerob = True

		self.case_x = x
		self.case_y = y
		self.x = self.case_x * 30
		self.y = self.case_y * 30
		print(self.structure)

pygame.init()
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
pygame.display.set_caption(titre_fenetre)
continuer = 1
while continuer:	

	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	continuer_jeu = 1
	continuer_accueil = 1

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
					choix = 'n1'		#On définit le niveau à charger

	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load(image_fond).convert()

		#Génération d'un niveau à partir d'un fichier

		mur = pygame.image.load(image_mur).convert()
		depart = pygame.image.load(image_depart).convert()
		arrivee = pygame.image.load(image_arrivee).convert_alpha()
		num_ligne = 0
		for ligne in structure:
			# On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				# On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':  # m = Mur
					fenetre.blit(mur, (x, y))
				elif sprite == 'd':  # d = Départ
					fenetre.blit(depart, (x, y))
				elif sprite == 'a':  # a = Arrivée
					fenetre.blit(arrivee, (x, y))
				num_case += 1
			num_ligne += 1


		#Création de Macgyver
		mg = Perso("images/mg_droite.png", structure)
		victoire = pygame.image.load("images/victoire.png").convert()
		defaite = pygame.image.load("images/perdu.png").convert()
		#placement des items
		tube = Item(image_tube, structure)
		seringue = Item(image_seringue, structure)
		ether = Item(image_ether, structure)
				
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
					mg.deplacer('droite')
				elif event.key == K_LEFT:
					mg.deplacer('gauche')
				elif event.key == K_UP:
					mg.deplacer('haut')
				elif event.key == K_DOWN:
					mg.deplacer('bas')			
			
		#Affichages aux nouvelles positions
		fenetre.blit(fond, (0,0))

		num_ligne = 0
		for ligne in structure:
			# On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				# On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':  # m = Mur
					fenetre.blit(mur, (x, y))
				elif sprite == 'd':  # d = Départ
					fenetre.blit(depart, (x, y))
				elif sprite == 'a':  # a = Arrivée
					fenetre.blit(arrivee, (x, y))
				num_case += 1
			num_ligne += 1
		fenetre.blit(mg.direction, (mg.x, mg.y)) #mg.direction = l'image dans la bonne direction
		if(structure[tube.case_y][tube.case_x] == 'i'):
			fenetre.blit(tube.image, (tube.x, tube.y))
		if(structure[seringue.case_y][seringue.case_x] == 'i'):
			fenetre.blit(seringue.image, (seringue.x, seringue.y))
		if (structure[ether.case_y][ether.case_x] == 'i'):
			fenetre.blit(ether.image, (ether.x, ether.y))
		pygame.display.flip()

		if structure[mg.case_y][mg.case_x] == 'a' and mg.compteur == 3:
			print("Victoire")

			continuer_jeu = 0
			fenetre.blit(victoire, (50, 50))
			pygame.display.flip()
			pygame.time.delay(5000)

		elif structure[mg.case_y][mg.case_x] == 'a' and mg.compteur != 3:
			print("Défaite")
			fenetre.blit(defaite, (50, 50))
			pygame.display.flip()
			pygame.time.delay(5000)
			continuer_jeu = 0

		#Victoire -> Retour à l'accueil
        
