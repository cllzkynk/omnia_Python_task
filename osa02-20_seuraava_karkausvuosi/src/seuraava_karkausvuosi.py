# Kirjoita ratkaisu tähän
flag=False
annetaanvuosi=int(input("Anna vuosi: "))
etsitaanvuosi=annetaanvuosi+1
while True:

   if (etsitaanvuosi%4==0 and etsitaanvuosi%100!=0) or etsitaanvuosi%400==0:
    flag=True
    break
   else :
    etsitaanvuosi+=1
if flag==True:
  print(f"Vuotta {annetaanvuosi} seuraava karkausvuosi on {etsitaanvuosi}")