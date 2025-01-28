# Kirjoita ratkaisu tähän
"""
Tee ohjelma, joka kysyy käyttäjältä kokonaisluvun. Jos käyttäjä syöttää negatiivisen luvun tai nollan, ohjelman suoritus päättyy. Muuten ohjelma tulostaa luvun kertoman.

Kertoma lasketaan kertomalla keskenään luku ja kaikki sitä pienemmät positiiviset kokonaisluvut. Esim. luvun 5 kertoma on 1 * 2 * 3 * 4 * 5 = 120.

Esimerkkisuorituksia:

Esimerkkitulostus
Anna luku: 3
Luvun 3 kertoma on 6
Anna luku: 4
Luvun 4 kertoma on 24
Anna luku: -1
Kiitos ja moi!

Esimerkkitulostus
Anna luku: 1
Luvun 1 kertoma on 1
Anna luku: 0
Kiitos ja moi!
"""

luku=1
while luku!=0: 
       luku=int(input("Anna luku: "))
       result=1
       num=1
       if luku<=0:
            
              break
       else :
              while num<=luku:
               
                     result=result*num
                     num+=1
              print(f"Luvun {luku} kertoma on {result}")
      
print("Kiitos ja moi!")          










"""while luku>1:
       
       result=result*luku
       str=f"{str}*{luku-1}"
       luku-=1
       if luku<=0:
        print("Kuitos ja moi!")
        break
       if luku==1:
        
        print(f"Luvun {num} kertoma on {result}")
        
        result=1
      
        luku=int(input("Anna luku: "))
       if luku<=0:
        print("Kiitos ja moi!")
        break
       
"""
       





