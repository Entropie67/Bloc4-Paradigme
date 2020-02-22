
# Voici une proposition de modification pour passer sur du fonctionnel
# Dans ce cas cependant, je pense que la lisibilité est préférable à la concision

with open('data/n1', "r") as fichier:
    structure_niveaua = list(map(lambda liste: list(filter(lambda x: x != '\n', liste)),
                                list(map(list, fichier))))

with open('data/n1', "r") as fichier:
    structure_niveau = []
    for ligne in fichier:
        ligne_niveau = []
        for sprite in ligne:
            if sprite != '\n':
                ligne_niveau.append(sprite)
        structure_niveau.append(ligne_niveau)

assert structure_niveaua == structure_niveau , "problème"
print("C'est bien la même chose")