###########################
# Loops                   #
# Auteur: Marlene Marchena#
###########################

# For loop

# Ex. 1 :

for i in range(20):
    print(f"Le valeur est : {i}")

# Ex. 2 :

for i in range(1, 20, 2):
    print(f"Le valeur est : {i}")

# Ex. 3 :

for i in range(1, 13):
    print(f"Le valeur {i} fois {i} est {i*i}")

# Ex. 4 :

liste_de_courses = ["lait", "bananes", "confiture", "sucre"]

for item in liste_de_courses:
    print(item)

# While loop

# Ex. 5 :

i = 0
while i < 10:
    print(i)
    i += 1

# Ex. 6 :

run = True
score = 0

while run:
    score += 1
    print(score)
    if score > 5:
        run = False
    print("Playing my game !")
print("You win ! ")

# Exercise 1
# Jusqu'à 12 fair un print de:
# La valeur 1 fois 1 est 1,
# La valeur 2 fois 2 est 4,
# etc

# Exercise 2
# Créer une liste de courses avec: lait, bananes,confituer et sucre
# Faire un print avec les items de la liste et le total de lettres de chaque item.
# Exemple:
# Le nombre de lettres du item lait est 4,
# Le nombre de lettres du item bananes est 7,
# etc

# Exercise 3
# Créer un programme pour demander au utilisateur sa pizza préférée.
# Faire un print avec "moi aussi j'aime {pizza}". Si l'utilisateur écrit 'sortir' repondre 'Au revoir' et arreter le programme.
# Example:
# Quelle est votre pizza préférée? Écrit sortir pour arreter le programme.
# Margarita
# Moi aussi j'aime Margarita
# Quelle est votre pizza préférée? Écrit sortir pour arreter le programme.
# Prosciutto
# Moi aussi j'aime Prosciutto
# Quelle est votre pizza préférée? Écrit sortir pour arreter le programme.
# sortir
# Au revoir
