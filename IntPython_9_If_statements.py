prenom = 'Jules'
age = 5

if  age < 18 :
    print("Tu n'es pas un adulte")
else:
    print("Tu es un adulte")

#avec eiif
if  age < 18 :
    print("Tu n'es pas un adulte")
elif age == 18 :
    print("Tu as 18 ans !")
else:
    print("Tu es un adulte")

# Exercise: Demande au utilisateur son prénom et âge et afiche le message suivant
# par example si prénom egale Jules
# si il a mois de 5 anes, " Jules, tu es en maternale"
# si il a plus de 5 anes et mois de 11 ans, "Jules, tu es à l'école primaire"
# si il a egale au plus de 11 anes et mois de 17 ans, "Jules, tu es à l'école secondaire"
# si il a plus de 17 ans, "Jules, tu as fini l'école"

#Solution:

prenom_util = input("Comment tu t'appelle ?")

age_util = int(input("Quel âge as-tu ?"))

if age_util < 5:
    print("Tu n'est pas à la l'école ")
elif (age_util <= 5 and age_util <= 12) :
    print("%s, Tu es à l'école primaire" % prenom_util )
elif (age_util > 12 and age_util <= 17) :
    print("%s, Tu es à l'école secondaire" % prenom_util)
else:
    print("%s, Tu as fini l'école" % prenom_util)
