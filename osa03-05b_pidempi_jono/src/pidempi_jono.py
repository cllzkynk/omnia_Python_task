# Kirjoita ratkaisu tähän
"""
Kirjoita ohjelma, 
joka kysyy käyttäjältä kaksi merkkijonoa
 ja tulostaa jonoista pidemmän
   (ts. sen, jossa on enemmän merkkejä).
     Jos jonot ovat yhtä pitkiä tulostetaan viesti 
     "Jonot ovat yhtä pitkät"

 

Esimerkkitulostus
Anna jono 1: moi
Anna jono 2: heippa
heippa on pidempi

Esimerkkitulostus
Anna jono 1: moikkelis koikkelis
Anna jono 2: heipparallaa
moikkelis koikkelis on pidempi

Esimerkkitulostus
Anna jono 1: moi
Anna jono 2: hei
Jonot ovat yhtä pitkät

"""

jono1=input("Anna jono 1: ")
jono2=input("Anna jono 2: ")
 


if len(jono1)>len(jono2):
    print(f"{jono1} on pidempi")
elif len(jono2)>len(jono1):
    print(f"{jono2} on pidempi")
else:print("Jonot ovat yhtä pitkät")