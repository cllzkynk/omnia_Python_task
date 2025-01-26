# Kirjoita ratkaisu tähän
"""
Kirjoita ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sitten
 merkkijonon merkit allekkain käänteisessä järjestyksessä lopusta alkuun.

Esimerkkitulostus
Anna merkkijono: heippa
a
p
p
i
e
h
"""
jono=input("Anna merkkijono: ")
index=len(jono)-1
while index>=0:
    print(jono[index])
    index-=1