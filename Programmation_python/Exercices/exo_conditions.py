#Question 1
semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

for i in semaine:
    if i=="vendredi":
        print("Chouette c'est vendredi")
    elif i=="samedi" or i=="dimanche":
        print("Repos ce week-end")
    else:
        print("Au travail")

for jour in semaine:
    if jour=="samedi" or jour=="dimanche":
        print("Repos ce week-end")
    elif jour=="vendredi":
        print("Chouette c'est vendredi")
    else:
        print("Au travail")

#Question 2
cours=["Python","Java","C++","NodeJs","JEE","JAVA","PYTHON","Jee","NODEJS"]
for i in range(len(cours)):
    if cours[i].isupper()==True:
        cours[i]=cours[i].lower()
print(cours)

#Question 3
liste=[89,74,76,18,51]
current_min=liste[0] 
for num in liste:
    if num < current_min:
        current_min=num
print(current_min)
        
#Question 4
cours=["IA","Big Data","Data science","IA","Big Data","Big Data","Data science","Big Data","IA"]
freq=[]
for cour in cours:
    if cour not in freq:
        freq.append(cour)
for i in range(len(freq)):
    print("Frequence de", freq[i], "est: ", cours.count(freq[i]))

#Question 5
notes=[14,9,13,15,12]
minimum=min(notes)
maximum=max(notes)

sum_notes=0
for i in notes:
    sum_notes+=i
mean=sum_notes/len(notes)
print(f"La moyenne est de: {mean:.2f}")

if mean<10:
    print("Pas de mention")
elif 10<=mean<12:
    print("Mention passable")
elif 12<=mean<14:
    print("Mention assez bien")
else:
    print("Mention bien")

#Question 6
for i in range(0,21):
    if i%2==0 and i<=10:
        print(f"{i} est un nombre pair")
    elif i%2!=0 and i>10:
        print(f"{i} est un nombre impair")

