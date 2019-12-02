##########################
#Tuples #
#Auteur: Marlene Marchena#
##########################
#Une tuple est une structure de donnée de python que nous
#permet de garder different valeurs.
#Le Tuples sont immuable, i.e, on me peut pas changer leur
#valeurs une fois initialize.
t0 = (1,2,3)

t1 =(0,1,2,True,"Paul")

t2 =(0.8,10,False,"Eric", True)

print(t1)
print(t2)

#On peut avoir une tuple dans une autre tuple
t3 = ("Roger",t1, (4,5), True)
print(t3)

#manipulation de Tuples
print(t2[3])
print(t2[2:]) #elements de la tuple apartir de la position 2
print(t2[-1]) #affiche le dernier element
print(t2[-2]) #affiche le avant dernier element
print(t2[:3]) #affiche le deux premier elements
# #La tuple est immuable !
# t2[3] = "Lucia"

#operations avec Tuples
x, y, z = t0
print(x)
print(y)
print(z)

t4 = t0 +t1
print(t4)
print(t4.count(2))
print(t4.index("Paul"))
