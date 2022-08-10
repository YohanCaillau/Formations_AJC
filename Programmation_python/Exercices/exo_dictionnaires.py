#Question 1
chaine=input("Tapez une chaine de caractères: ")

def count_caracters(chaine):
    nbmin=0
    nbmaj=0
    chiffre=0
    special=0
    d=dict()    
    for i in chaine:
        d['nbmin']=nbmin
        d['nbmaj']=nbmaj
        d['chiffre']=chiffre
        d['special']=special
        if i.isnumeric():
            chiffre+=1
        elif i.isupper():
            nbmaj+=1
        elif i.islower():
            nbmin+=1
        else:
            special+=1
    print(d)

#Question 3

dict_1={"ML":15,"DL":17,"Python":19}

dict_2={"ML":5,"DL":7,"Python":9}

dict_3={"ML":10,"DL":11,"Python":12}


#On créé un dictionnaire qui va contenir les autres
dic_total={}

#On ajoute les dictionnaires un à un
dic_total.update(dict_1)
dic_total.update(dict_2)
dic_total.update(dict_3)
print(dic_total)

#On ajoute les dictionnaires via la boucle for
for d in [dict_1, dict_2, dict_3]:
    dic_total.update(d)

print(dic_total)


#Question 4

notes_etud={"Marc":5, "Marie":11, "Toto":4, "Tata":9, "Nono":12}
etudAdmis={}
etudNonAdmis={}
for key, val in notes_etud.items():
    if val <=10:
        etudAdmis[key]=val
    else:
        etudNonAdmis[key]=val
print(f" étudiants admis : {etudAdmis}, étudiants non admis {etudNonAdmis}")

#Question 5

n=int(input("Entrer la valeur de n : "))

#On crée un dictionnaire vide qui va contenir les nombres n et leurs carrés
d = dict()

#On fait le parcours des entiers de 1 à n
for i in range(1,n+1):
    d[i]=i*i
print(d)

def square_dict():
    n=int(input("Entrer la valeur de n : "))
    sqr_dict={}
    for n in range(1,n+1):
        sqr_dict[n] = n**2
    print(sqr_dict)

#Question 6
ch=input("une chaine: ")
d=dict({})

#for i in len(ch):

#Question 7
def list_dict(l):
    #création d'un dictionnaire vide pour récupérer les résultats
    dict_parity=dict()

    #parcourir les éléments de la liste et tester leur parité
    for x in l:
        if x%2 ==0:
            dict_parity[x] = 'Pair'
        else:
            dict_parity[x] = 'Impair'
    return dict_parity

#Faire un test
l=[24,14,3,36,41,22,15]
print(list_dict(l))
    
#Question 8
X={"a","b","c","d"}
Y={"s","d","d"}

print ("c appartient-il à X ?", "c" in X)
print ("c appartient-il à Y ?", "c" in Y)
print("X-Y : ", X-Y)
print("Y-X : ", Y-X)
print("Y and X : ", Y&X)
print("Intersection : ", X|Y)

#Question 10
def somme(*args):
    resultat=0
    for nombre in args:
        resultat+=nombre
    return resultat


#Question 11
def unDictionnaire(**kargs):
    return kargs

print(" appel avec des paramètres nommés ")
print(unDictionnaire(a=23, b=42))
print(" appel avec un dictionnaire décompressé ".center(60, '-'))
mots={'d':85,'e':14,'f':9}
print(unDictionnaire(**mots))










