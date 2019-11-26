# ##########################
# #     Enchaînement       #
# #Auteur: Marlene Marchena#
# ##########################
txt1 = "Bonjour"
txt2 = "tout le monde"
print(txt1 + txt2)

# #Exercice
# #Faire un print du string Bonjour tout le monde"

# #Trois methodes:
#
# #1. On peut utiliser simplement un space avec " "
print(txt1 + " " + txt2)
#
# #2. On peut utiliser %s, en sort de marqueur
print("Ici mon texte: %s %s" % (txt1 , txt2))
#
# #3. On peut utiliser la function format()
print("Ici mon texte: {0} {1}".format(txt1,txt2))
# # #Ça marche sans la position aussi
print("Ici un autre methode: {} {}".format(txt1,txt2))
# # #On peut aussi utiliser un alias
print("Ici mon texte: {x} {y}".format(x=txt1,y=txt2))

# #en Python 3.6 et en diante on peut utiliser
print("À partir de python 3.6 on peut écrire: "f"{txt1} {txt2}")

#Exercice 1:
#1.Creer une variable nom avec ton nom
#2. Creer une variable message que contient un string "Bonjour %s ! Comment ça va ?"
#3. Aficher avec la function print le message avec le string de la variable nombre

#nom = "Marlene"
#message = "Bonjour %s ! Comment ça va ?"
#print("Bonjour %s ! Comment ça va ?" % nom)
#print( message % nom)

#Exercice 2:
#1.Creer trois variables avec les nombres 3, 4 et 12
#2.Utiliser le methode 3 de concatenation pour fair un Print de:
#3. "La operation 3 fois 4 est egal à 12"
