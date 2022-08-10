#Question 1

with open ("notes.txt", "r") as file:
    print(file.readlines())

notes=[]
sum_notes=0
with open ("C:\\Users\\yohan\\OneDrive\\Bureau\\Formations\\Cours\\Programmation_python\\notes.txt", "r") as file:
    for ligne in file:
        notes.append(float(ligne))
    print(notes)
    for i in notes:
        sum_notes+=i
mean=sum_notes/len(notes)
print(f"La moyenne est de: {mean:.2f}")


#Question 2
notes=[]
with open ("notes.txt", "r") as file1, open("notes2.txt", "w") as file2:
    for ligne in file1:
        notes.append(float(ligne))
    print(notes)
    for i in notes:
        if i <10:
            file2.write(f"{i} -> recalé\n")
        else:
            file2.write(f"{i} -> admis\n")

with open ("notes2.txt","r") as file2:
    print(file2.readlines())

#Question 3
name=input("Votre nom svp: ")
with open (f"{name}.txt", "w")as file:
    writing=input("que voulez vous écrire: ")
    file.write(writing)
print("Votre texte est sauvegardé")

#Question 4
with open ("multi.txt","w") as file:
    i = 1
    while i <= 10:
        nb = 1
        while nb <= 10:
            #print(i*nb, end = " ")
            multiplication=(i*nb)
            file.write(str(multiplication)+ "\n")
            nb = nb + 1
        print("")
        i = i + 1

file=open("multiplication.txt","w")
file.write(".-------------------------------")
for n in range(1,10):
    file.write(".-------------------------------")
    file.write("\n")
    c=str("La table de multiplication de : ")+ str(n) +" est :"
    file.write(c)
    for i in range(1,10):
        y=str(i)+" x"+ str(n) + " = "+str(i*n)
        file.write(y)
        file.write("\n")


#Question 5
with open ("test.txt", "r") as file1, open("copy.txt", "w") as file2:
    for ligne in file1:
        if ligne[0:1] == "#":
            continue
        else:
            file2.write(ligne)

with open ("copy.txt","r") as file:
    print(file.readlines())

#Question 6
with open("notes.txt", 'r') as file:
    num_lines = sum(1 for line in file)
    print('Total lines:', num_lines)

with open("notes.txt", 'r') as file:
    count = 0
    for ligne in file:
        if ligne != "\n":
            count += 1
print('Total Lines', count)

#Question 7
with open("Definition.txt","w") as file:
    file.write("Définition= Python est un langage de programmation interprété, \n multiparadigme et multiplateformes. Il favorise la programmation impérative structurée, fonctionnelle et orientée objet")

with open("Definition.txt","r") as file:
    print(file.readlines())

#Question 8
with open("test.txt","r") as file1, open("Definition.txt","a") as file2:
    for ligne in file1:
        file2.write(ligne)

with open("Definition.txt","r") as file:
    print(file.readlines())

