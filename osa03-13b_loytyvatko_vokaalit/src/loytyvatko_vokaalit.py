# Kirjoita ratkaisu tähän

"""
Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa 
sitten tiedon löytyvätkö vokaalit a, e ja o merkkijonosta.

Voit olettaa, että merkkijono on syötetty kokonaan pienillä kirjaimilla.
Katso mallia esimerkkitulostuksesta.

 
Esimerkkitulostus
Anna merkkijono: heippa sulle
a löytyy
e löytyy
o ei löydy

Esimerkkitulostus
Anna merkkijono: moi
a ei löydy
e ei löydy
o löytyy

"""

mjono = input("Anna merkkijono: ")
vokaalit = "aeo"
indeksi = 0
 
while indeksi < len(vokaalit):
    vokaali = vokaalit[indeksi]
    if vokaali in mjono:
        print(vokaali, "löytyy")
    else:
        print(vokaali, "ei löydy")
    indeksi += 1
 










"""str=input("Anna merkkijono: ")
steps=0
flag_a=0
flag_e=0
flag_o=0

while steps<=(len(str)-1):
    if str[steps]=="a":
     flag_a+=1
    if str[steps]=="e":
     flag_e+=1
    if str[steps]=="o":
     flag_o+=1
    steps+=1
    
print("a löytyy")  if flag_a!=0 else print("a ei löydy")
print("e löytyy")  if flag_e!=0 else print("e ei löydy")
print("o löytyy")  if flag_o!=0 else print("o ei löydy")"""