##########################
#Listes #
#Auteur: Marlene Marchena#
##########################

li0 =["Juan", 4, True, 0.34]
print(li0)

li1 = [1,2,3]
print(li1)

len(li0)
len(li1)

print(li0[0].upper())

li0.reverse()
print(li0)

li1.sort()
print(li1)

a=[1,2,3] ; b=[4,5] ; a.extend(b)
print(a)

#Changer, ajouter et enlever
li0 =["Juan", 4, True, 0.34]
li1 = [1,2,3]
li0[0]="Joana"
print(li0)

# En raison de leur mutabilité, les listes ont de nouvelles opérations
li1.append(4)
print(li1)

li0.insert(2,"happy")
print(li0)

li1.remove(4) #remove last element
print(li1)

popped = li0.pop() #remove last element, but you can still use it
print(li0)
print(popped)

#Exercice 1
# 1. Créer une liste cars avec: Toyota, Jaguar, BMW, Twingo
# 2. Ajuter à la liste Peugeot
# 3. Changer BMW par Tesla
# 4. Créer une déuxieme liste mycars avec Ferrarie et Ford
# 5. Augmenter la liste car avec les elements de la liste favorites
# 6. Inserir après Twingo la voiture Mercedes

# #Les éléments de une liste sont des pointeurs
# li2 = li1
# print(li2)
#
# print(li1 == li2)
#
# #Si on change la valeur de la position zéro
# li1[0] = 7
# #On va changer les deux listes
# print(li1)
# print(li2)
#
# #Pour fair une copie on dois utiliser le symbol [:]
# # (on fais une Deep copy)
# li2 = li1 [:] # on fait une copie
# print(li2)
# li1[0] = 1 #on change li1
# print(li1)
# print(li2) ##On ne changes pas li2
