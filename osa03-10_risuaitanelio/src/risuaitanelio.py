# Kirjoita ratkaisu tähän
"""Laajenna edellistä niin, että käyttäjä syöttää myös piirrettävien rivien määrän

Esimerkkitulostus
Leveys: 10
Korkeus: 3
##########
##########
##########"""


leveys=int(input("Leveys: "))
korkeus=int(input("Korkeus: "))



while korkeus>0:
    print("#"*leveys)
    korkeus-=1