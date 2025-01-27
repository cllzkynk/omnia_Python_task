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
index=len(sana)-1
sana_box=""
while index>=0:
    sana_box=sana[index:index+1]+sana_box
    print(sana_box)
    index-=1


"""
merkkijono = input("Anna merkkijono: ")
 
alku = len(merkkijono) - 1
while alku >= 0:
    print(merkkijono[alku:])
    alku -= 1
    

"""
    