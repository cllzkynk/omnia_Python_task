# Kirjoita ratkaisu tähän
"""
Tee ohjelma, joka kysyy käyttäjältä sanan ja kertoo,
 ovatko sen toinen ja toiseksi viimeinen merkki samoja.

Esimerkkitulostus
Anna sana: python
Toinen ja toiseksi viimeinen kirjain eroavat

Esimerkkitulostus
Anna sana: pascal
Toinen ja toiseksi viimeinen kirjain on a
"""

sana=input("Anna sana: ")
if len(sana) > 1 and  sana[1]==sana[-2]:
    print(f"Toinen ja toiseksi viimeinen kirjain on {sana[1]}")
else : print("Toinen ja toiseksi viimeinen kirjain eroavat")