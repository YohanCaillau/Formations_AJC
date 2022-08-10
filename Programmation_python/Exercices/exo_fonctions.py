def somme(x,y):
    return(x+y)

def sous(x,y):
    return(x-y)

def hello():
    print("hi")
    
def somme_ent(a,b):
    if isinstance (a,int):
        return(a+b)

#Question 1
def multiplication(x,debut,fin,pas):
    result=[]
    for i in range(debut,fin+1,pas):
        res=x*i
        result.append([str(i)+"x"+str(x),res])
        #result.append(res)
        #print(x*i)
    return result

#Question 2
def cube(x):
    return x**3

#Question 3
pi=3.14
def calcul_volume_sphere(r):
    V=4/3*pi*cube(r)
    return V

#ou import math et utiliser math.pi

#Question 4
def Poly_fct(x):
    fct=4*cube(x)+2*x-1
    return fct

#Question 5
def calc_test(fonction,borne_inf,borne_sup,nb_pas):
    f_values=[]
    if borne_inf>borne_sup:
        print("Erreur")
    else:
        pas=(borne_sup - borne_inf)/nb_pas
        for i in range(nb_pas):
            f_values.append(fonction(borne_inf+i*pas))
    return f_values
#f_val=calc_test(Poly_fct, 3.2,8.9, 100)
#print(f_val)

#Question 6
def moyenne(liste=[]) :
    somme = sum(liste)
    nb_elements = len(liste)
    moyenne = somme / nb_elements
    return moyenne

#Question 7
def somme_list(liste=[]):
    somme=sum(liste)
    return somme

#Question 8
def min_max_liste(liste=[]):
    minimum=min(liste)
    maximum=max(liste)
    return minimum, maximum

#Question 9
def doublon(liste=[]):
    nvllListe = list(set(liste))
    return nvllListe


def doublon_2(liste=[]):
    new_list = []
    for i in liste :
        if i not in new_list:
            new_list.append(i)
    #return(new_list)
    print(new_list)

#Question 10
import shutil

def copy(path, new_path):
    filePath = shutil.copy(path, new_path)
    #return filePath
    print(f"{path} a été copié dans {new_path}")

def copy_file(source, destination):
    with open(source,"r") as source_file, open(destination,"w") as dest_file:
        for line in source_file:
            dest_file.write(line)
    







    
    
