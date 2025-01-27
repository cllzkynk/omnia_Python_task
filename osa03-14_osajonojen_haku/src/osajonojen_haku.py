# Kirjoita ratkaisu tähän

sana = input("Sana: ")
merkki = input("Merkki: ")
 
kohta = 0
 
while kohta + 3 <= len(sana):
    if sana[kohta] == merkki:
        print(sana[kohta:kohta+3])
    kohta += 1
 




"""

sana=input("Sana: ")
merkki=input("Anna merkki :")

index=0

while  index<len(sana):
    if merkki==sana[index] and index+2<len(sana):
        print(sana[index:index+3])
      
    index+=1
"""