# Kirjoita ratkaisu tähän
"""
Tee ohjelma, joka pyytää käyttäjältä merkkijonoja
 ja tulostaa kunkin merkkijonon oheisen esimerkin
   mukaisesti alleviivattuna. Ohjelman suoritus päättyy, 
   kun käyttäjä syöttää tyhjän merkkijonon, eli merkkijonon jonka pituus on 0.

Esimerkkitulostus
Anna merkkijono: Moi kaikki!

Moi kaikki!
-----------
Anna merkkijono: Tämä on testijono

Tämä on testijono
-----------------
Anna merkkijono: a

a
-
Anna merkkijono:
"""
text="a"
while text!="":
    text=input("Anna merkkijono: ")
    print(text)
    print("-"*len(text))


    """
    while True:
    merkkijono = input("Anna merkkijono: ")
    if merkkijono == "":
        break
    print(merkkijono)
    print(len(merkkijono) * "-")
    
    """