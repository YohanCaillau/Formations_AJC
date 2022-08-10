test=["SGBD","MySql","SQLSERVER","Python"]
#Méthode 1
#for i in range(len(test)):
#    print(test(i))

#print("méthode 1: c'est fini")

#Méthode 2
for i in test:
    print(i)
    
print("méthode 2: c'est fini")

for i in test[0:4]:
    print(i)
    
print("4 premières valeurs")

#Méthode 3

compteur=0
while (compteur<len(test)):
    print(test[compteur])
    compteur=compteur+1
print("méthode 3: c'est fini")

semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

#Question 2: Méthode 1

for i in semaine[0:5]:
    print(i)

#Méthode 2

j=5
while j<len(semaine):
    print(semaine[j])
    j +=1

#Question 3
for i in range(1,10):
    print(i, end='')

#Question 4
impairs=[1,3,5,7,9,11,13,15,17,19,21]

pair=[]
for i in impairs:
    pair.append(i+1)
print(pair)

pairs=[i+1 for i in impairs]
print(pairs)

#Question 5
notes=[14,9,6,8,12]

c=0
for i in notes:
    c=c+i
moyenne=c/len(notes)
print(moyenne)

#Question 6
num_pair=list(range(2,21,2))

produit=num_pair[0]
pair=[]
for i in range(len(num_pair)-1):
    produit*=num_pair[i+1]
    print(produit)
    produit=num_pair[i+1]
    pair.append(produit)
print(pair)

#Question 7
for i in range(1,11):
    for j in range(i):
        print("*", end="")
    print("")

#Question 8
nombre_ligne=int(input("Nombre de ligne svp: "))
for i in range(nombre_ligne,0,-1):
    print("*"*i)

#Question 9
étoile="*"
for i in range(1,11):
    print(f"{étoile*i:>10}")

nombre=int(input("Nombre de ligne svp: "))
for i in range(1,nombre+1):
    print(" "*nombre,"*"*i)
    nombre-=1

#Question 10
étoile="*"
for i in range(1,21,2):
    print(f"{étoile*i:^21s}")

for i in range(1,11):
    print((10-i)*" ","* "* i)







