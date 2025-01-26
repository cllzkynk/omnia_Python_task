# Kirjoita ratkaisu tähän
"""
Tee edellisestä ohjelmasta hieman kehittyneempi versio,
 joka tulostaa lopputuloksen lisäksi myös sen miten kyseinen summa lasketaan:
Mihin asti: 18
Laskettiin 1 + 2 + 3 + 4 + 5 + 6 = 21
 
 """


num_asti=int(input("Mihin asti: "))
num=int(1)
sum=1
string="1"
while sum<num_asti:
   num+=1
   sum+=num  
  
   string=string+" + "+str(num)
   
   
   
print(f"Laskettiin {string } = {sum}")
"""
asti = int(input("Mihin asti: "))
luku = 1
summa = 1
while summa < asti:
    luku += 1
    summa += luku
print(summa)
"""