lista=[1, 2, 3, 4, 5]
arvo=1
 
while arvo !=-1:
     
    index=int(input("Anna index: "))
    if index==-1:
        break
    if index<=-2 or index>=len(lista):
        continue
    arvo=int(input("Anna arvo: "))
    lista[index]=arvo
    print(lista)