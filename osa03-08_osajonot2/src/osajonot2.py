# Kirjoita ratkaisu tähän

"""
Tee ohjelma, joka kysyy käyttäjältä merkkijonon 
ja tulostaa sitten kaikki sen viimeiseen merkkiin päättyvät 
osajonot pituusjärjestyksessä.
Esimerkkitulostus
Anna merkkijono: testi
i
ti
sti
esti
testi
"""

sana=input("Anna sana: ")
pituus = len(sana)-1
while pituus>=0:
    print(sana[pituus:-1])
    pituus -= 1