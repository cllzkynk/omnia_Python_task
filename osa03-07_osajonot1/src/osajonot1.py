# Kirjoita ratkaisu tähän
"""
Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sitten kaikki sen ensimmäisestä merkistä alkavat osajonot pituusjärjestyksessä.

Esimerkkitulostus
Anna merkkijono: testi
t
te
tes
test
testi
"""
sana=input("Anna sana: ")
index=0
sana_container=""
while index<len(sana):
    sana_container=sana_container+sana[index]
    print(sana_container)
    index+=1



"""
merkkijono = input("Anna merkkijono: ")
 
pituus = 1
while pituus <= len(merkkijono):
    print(merkkijono[0:pituus])
    pituus += 1

"""