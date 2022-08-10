import ast
from collections import Counter
from statistics import mean

with open("NotesEtude__193__0.txt", 'r') as file1:
    note=file1.read()
    Notes_etudiant=ast.literal_eval(note)
    #print(Notes_etudiant)

def add_notes(nom_etudiant, note):
    global Notes_etudiant
    if nom_etudiant in Notes_etudiant:
        Notes_etudiant[nom_etudiant].update(note)
    else:
        Notes_etudiant[nom_etudiant]=note

def show_note(nom_etudiant):
    #global Notes_etudiant
    if nom_etudiant in Notes_etudiant:
        print(Notes_etudiant[nom_etudiant])

def occurence_note(nom_etudiant):
    if nom_etudiant in Notes_etudiant:
        compte= Counter(Notes_etudiant[nom_etudiant].values())
        print(compte)
    else:
        print("Etudiant n'existe pas")

def moyenne(nom_etudiant):
    count=0
    somme=0
    if nom_etudiant in Notes_etudiant:
        for key in Notes_etudiant[nom_etudiant]:
            if isinstance(Notes_etudiant[nom_etudiant][key],int)or isinstance(Notes_etudiant[nom_etudiant][key],float):
                count +=1
                somme +=Notes_etudiant[nom_etudiant][key]
        moy=somme/count
        return moy

def validation():
    for nom_etudiant in Notes_etudiant:
        moy=moyenne(nom_etudiant)
        if moy<12:
            Notes_etudiant[nom_etudiant]['validation']='non validé'
        else:
            Notes_etudiant[nom_etudiant]['validation']='validé'

def percent():
    somme=0
    for nom_etudiant in Notes_etudiant:
        if Notes_etudiant[nom_etudiant]['validation']=='validé':
            somme+=1
    poucentage_reussite=(somme/len(Notes_etudiant))*100
    Notes_etudiant[nom_etudiant]['pourcentage']=poucentage_reussite

    return poucentage_reussite, somme, len(Notes_etudiant)

def validation_nom(nom):
    if moyenne(nom)<12:
        print("année non validée")
    else:
        print("année validée")

def add_files():
    with open("notes_exo.txt","w")as file:
        file.write(str(Notes_etudiant))
        print(file)
        
            
#programme principal
if __name__=="__main__":
    occurence_note('etudiant_1')
    moyenne('etudiant_1')
    validation()
    percent()
    add_files()


