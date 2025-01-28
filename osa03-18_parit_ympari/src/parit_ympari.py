# Kirjoita ratkaisu tähän
"""
Tee ohjelma, joka tulostaa luvut 1:stä käyttäjän antamaan lukuun. Luvut on kuitenkin käännetty pareittain ympäri.

Anna luku: 5
2
1
4
3
5

 
num=input("Anna luku: ")
luku=int(num)

scanner=2
step=1








while (luku)>0:
   
    if step%2!=0:
     
     if luku!=1:
      print(scanner)
     print(scanner-1)
    else :
     
     if luku!=1:
      print(scanner)
      
     print(scanner-1)

     
    scanner+=2
    luku-=2
    step+=1
"""

luku = int(input("Luku: "))
 
kohta = 1
while kohta+1 <= luku:
    print(kohta+1)
    print(kohta)
    kohta += 2
 
if kohta <= luku:
    print(kohta)