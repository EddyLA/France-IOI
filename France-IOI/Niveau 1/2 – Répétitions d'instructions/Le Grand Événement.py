from robot import *
haut()
# Allers-retours sur les 9 lignes du haut, pour les 8 premi�res colonnes
for loop in range(4):
   for loop in range(8):
      haut()
   droite()
   for loop in range(8):
      bas()
   droite()
# Deux derni�res colonnes avec redescente jusqu'en bas
for loop in range(8):
   haut()
droite()
for loop in range(9):
   bas()
# Et on rentre � la position de d�part
for loop in range(9):
   gauche()

#Eddydev