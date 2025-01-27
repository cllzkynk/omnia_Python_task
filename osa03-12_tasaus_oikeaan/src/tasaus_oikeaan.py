# Kirjoita ratkaisu tähän

"""
Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sen niin, että tulostetuksi tulee tasan 20 merkkiä. Jos merkkijono on lyhyempi, alkuun tulee tarvittava määrä tähtiä *.

Voit olettaa, että syötetyssä merkkijonossa on enintään 20 merkkiä.

Esimerkkitulostus
Sana: python

**************python
Esimerkkitulostus
Sana: pitkämerkkijono

*****pitkämerkkijono
Esimerkkitulostus
Sana: tosipitkämerkkijono

*tosipitkämerkkijono
"""

sana=input("Sana: ")
merkki="*"
print(f"{merkki*(20-len(sana))}{sana}")


"""

sana = input("Sana: ")
 
tasattu = (20 - len(sana)) * "*" + sana
 
print(tasattu)
 

"""