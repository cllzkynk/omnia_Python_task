 
# Kirjoita ratkaisu tähän
"""
Tee ohjelma, joka lukee käyttäjältä positiivisen kokonaisluvun N. Ohjelma tulostaa sen jälkeen luvut väliltä -N...N nollaa lukuunottamatta. Jokainen luku tulostetaan omalle rivilleen.
 
Esimerkiksi
 
Esimerkkitulostus
Anna luku: 4
-4
-3
-2
-1
1
2
3
4
"""
 
 
luku=int(input("Anna positiivinen kokonaisluku: "))
i=-luku
while i<=luku:
     if i==0:
          i+=1
     print(i)
     
     i+=1


