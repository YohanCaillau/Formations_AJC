import xml.dom.minidom
import os
import xml.etree.ElementTree as et

os.chdir

print("****************************")
print("Variable 1 using xml.dom.minidom")

var1=xml.dom.minidom.parse("data.xml")
print(var1)

elements=var1.getElementsByTagName("item")
print(f"Nous avons {elements.length} elements")

for i in elements:
    print(i.getAttribute("nom"))

print("\n****************************")
print("Variable 2 using ElementTree")

var2=et.parse("data.xml")
root=var2.getroot()
print(root.tag)

print("\n****************************")
print("Variable 3 using ElementTree")


#change product by racine
var3='''<racine>
<Software>
<item nom="ABC">Convertisseur PDF</item>
<prix>100</prix>
<version>1.2</version>
</Software>
<Hardware>
<item nom="XYZ">Clavier</item>
<prix>20</prix>
<garantie>2 ans</garantie>
</Hardware>
</racine>'''

root=et.fromstring(var3)
print(root.tag)

#la balise du premier enfant de l'élément racine
print("\nLe premier enfant de la racine : ",root[0].tag)

#afficher toutes les balises
print("\nLes balises sont : ")
for x in root[0]:
      print(x.tag)

#afficher tous les textes
for i in range(len(root)):
    print(f"\nLe sub-élémént numéro {i}: est un {root[i].tag}")
    for a in root[i]:
        print(f"{a.tag}:{a.text}")


###########
        
print("\n****************************")
print("Exemple d'ouverture de fichier xml avec open")
with open("data.xml") as file:
    print(file)
    
###########
