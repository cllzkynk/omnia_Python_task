# Kirjoita ratkaisu tähän

# Kirjoita ratkaisu tähän
# Kirjoita ratkaisu tähän
jono=input("Anna merkkijono: ")
osa=input("Anna osa: ")
osanlen=len(osa)
index=0
count=0
while index<=len(jono):

 
       
   if osa==jono[index:index+osanlen]:
      count+=1
 

   if count==2:
       print(f"Osajonon toinen esiintymä on kohdassa {index}.")
       break
   if osa==jono[index:index+osanlen]:
   
      index=index+osanlen-1
   
   index=index+1


if count<2:
   print("Osajono ei esiinny merkkijonossa kahdesti.")