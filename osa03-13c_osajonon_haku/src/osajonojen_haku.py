# Kirjoita ratkaisu tähän

"""Tee ohjelma, joka kysyy käyttäjältä merkkijonoa ja yksittäistä merkkiä. Ohjelma tulostaa merkkijonosta löytyvän ensimmäisen kolmen merkin pituisen osajonon, jonka alkukirjain on käyttäjän syöttämä merkki. Voit olettaa, että merkkijono on vähintään kolmen merkin pituinen.

Esimerkkitulostus
Sana: apinatalo
Merkki: a
api

Esimerkkitulostus
Sana: banaani
Merkki: n
naa

Esimerkkitulostus
Sana: tomaatti
Merkki: x"""

sana=input("Sana: ")
merkki=input("Anna merkki :")

index=0

while  index<len(sana):
    if merkki==sana[index] and index+2<len(sana):
        print(sana[index:index+3])
        break
    index+=1




"""
sana = input("Sana: ")
merkki = input("Merkki: ")
 
kohta = sana.find(merkki)
if kohta!=-1 and len(sana)>=kohta+3:
    print(sana[kohta:kohta+3])

"""