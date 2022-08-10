#Question 1

#Exercice 1

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_perimeter(self):
        return ((self.length+self.width)*2)
    
    def rectangle_area(self):
        return self.length*self.width

class Parallelepipede(Rectangle):
    def __init__(self, l, w, h):
        Rectangle.__init__(self,l,w)
        self.height = h
        
    def get_length(self):
        return self.length

    def get_width(self):
        return self.width
    
    def set_heigth(self, value):
        self.heigth=value
 
    def parallelepipede_volume(self):
        return self.length*self.width*self.height


newRectangle = Rectangle(12, 10)
newParallelepipede = Parallelepipede(12,10,10)
print(newRectangle.rectangle_perimeter())
print(newRectangle.rectangle_area())
print(newParallelepipede.parallelepipede_volume())
print(Parallelepipede.get_length(newParallelepipede))
Parallelepipede.set_heigth(newParallelepipede, 11)
print(newParallelepipede.heigth)

#Exercice 2

class CompteBancaire:
    def __init__(self, num, nom, solde):
        self.num = num
        self.nom = nom
        self.solde = solde
        
    def versement(self, argent):
        self.solde = self.solde + argent
    
    def retrait(self, argent):
        if(self.solde < argent):
            print("Impossible d'effectuer l'opération. Solde insuffisant !")
        else:
            self.solde = self.solde - argent
    
    def agios(self):
        self.solde =self.solde*95/100
    
    def afficher(self):
        print("Compte numéro : " , self.num)
        print("Nom & Prénom : ", self.nom)
        print(" Solde  : ", self.solde , " DH ")
        print("Sauf erreur ou omisssion ! ")


if __name__=='__main__':       
    monCompte = CompteBancaire(16168891, " Bouvier David", 22300)
    monCompte.versement(1500)
    monCompte.retrait(24000)
    monCompte.agios()
    monCompte.afficher()

#Exercice 5

class myString:
    def __init__(self,s):
        self.s = s
        
    def append(self,x):
        self.s = self.s + x
        return self.s

    def pop(self,i):
        s1 = self.s[0:i]
        s2 = self.s[i+1:len(self.s)]
        return s1+s2

# Tester la classe  
if __name__=='__main__':       
    S1 = myString("hello")
    S2 = myString("bonjour")
    print(S1.append(" world !")) # affiche 'hello world !'
    print(S2.pop(2)) # affiche 'bojour'


    

    
