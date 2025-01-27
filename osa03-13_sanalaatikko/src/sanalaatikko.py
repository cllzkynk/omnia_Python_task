# Kirjoita ratkaisu tähän

"""
Tee ohjelma, joka kysyy käyttäjältä sanaa ja tulostaa sanan tähtiraameihin,
 joissa sana on keskellä. Raamien leveys on 30 merkkiä, ja voit olettaa,
   että sana mahtuu raameihin.

Huom! Jos sanan pituus on pariton,
 voit tulostaa sanan kumpaan tahansa mahdollisista keskikohdista.

Esimerkkitulostus
Sana: koe

******************************
*            koe             *
******************************

Sana: python

******************************
*           python           *
******************************

"""

sana=input("Sana: ")
keski=int((28-(len(sana))))//2

blank=" "*keski
if len(sana)%2==0:
    blank2=" "*keski 
else : blank2=" "*(keski+1)

print("*"*30+"\n*"+blank+sana+blank2+"*\n"+"*"*30)


"""
sana = input("Sana: ")
 
print("*" * 30)
alkuvalit = (28 - len(sana)) // 2
loppuvalit = alkuvalit
 
# Jos sanan pituus on pariton, lisätään loppuväliin 1
# jotta saadaan täydet 30 merkkiä
if len(sana) % 2 != 0:
    loppuvalit += 1
 
print("*" + alkuvalit * " " + sana + loppuvalit * " " + "*")
print("*" * 30)
 
"""

