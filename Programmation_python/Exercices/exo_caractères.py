#Demander une chaine de caractères
#chaine=input("Entrez une chaine de caractères: ")
p="T"
length=len(chaine)

#Boucle pour parcourir la liste
for i in range(0,length):
    if(chaine[i]==p):
        print(f"le caractère T existe dans la position: {i}")

def fct(chaine,p):
    length=len(chaine)
    for i in range(0,length):
        if(chaine[i]==p):
            print(f"le caractère {p} existe dans la position: {i}")

def locate_caracters(chaine):
    letters = chaine.find("i")
    numbers = [int(car)for car in chaine.split() if car.isdigit()]
    print(f"La lettre existe : {letters} et les chiffres sont : {numbers}")


ch = "P@#ynMo@HameD26at^&i5ve"

#Pour séparer chaque caractères
#print(list(ch))

def count_caracters(chaine):
    nbmin=0
    nbmaj=0
    chiffre=0
    special=0
    for i in chaine:
        if i.isnumeric():
            chiffre+=1
        elif i.isupper():
            nbmaj+=1
        elif i.islower():
            nbmin+=1
        else:
            special+=1
    return [nbmin,nbmaj,chiffre,special]


    




          

