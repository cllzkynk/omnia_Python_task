# Kirjoita ratkaisu tähän
vuosi=int(input("Anna vuosi: "))

if (vuosi%4==0 and vuosi%100!=0) or vuosi%400==0:
   print("Vuosi on karkausvuosi.")
else :
    print("Vuosi ei ole karkausvuosi.")



"""
Bir yıl 4'e bölünebiliyorsa artık yıldır. 
Ancak, bir yıl 100'e bölünebiliyorsa, 
yalnızca 400'e de bölünebiliyorsa artık yıldır.

"""