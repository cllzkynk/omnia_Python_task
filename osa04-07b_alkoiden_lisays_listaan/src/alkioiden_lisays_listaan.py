# Kirjoita ratkaisu tähän

monta=int(input("Kuinka monta lukua: "))
monta1=monta
lista=[]
 
while monta>0:
    lista.append(int(input(f"Anna luku {monta1+1-monta} : ")))
    monta-=1
 
print(lista)
 