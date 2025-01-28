# Kirjoita ratkaisu tähän

"""Tee ohjelma, joka kysyy käyttäjältä luvun ja tulostaa sitten lukuja vuorotellen seuraavien esimerkkien mukaisesti.

Esimerkkitulostus
Anna luku: 5
1
5
2
4
3
"""

luku = int(input("Luku: "))
 
kohta = 1
while kohta <= luku/2:
    print(kohta)
    print(luku+1-kohta)
    kohta += 1
 

if luku%2!=0:
    print(kohta)
