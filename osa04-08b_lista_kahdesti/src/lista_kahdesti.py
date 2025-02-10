# Kirjoita ratkaisu tähän
# Kirjoita ratkaisu tähän
lista=[]
lista2=[]
while True:
 luku=int(input("Anna luku:  "))
 lista2=lista
 if luku==0:
    print("Moi!")
    break
 lista.append(luku)
 print(f"Lista: {lista}")
 lista2=lista.copy()
 lista2.sort()
 print(f"Järjestettynä: {lista2}")