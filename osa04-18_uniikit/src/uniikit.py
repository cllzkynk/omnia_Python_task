# tee ratkaisu tänne
def uniikit(lista):
    uusi_lista=[]
    lista.sort()
    check=True
    for i in range(len(lista)):
       if i==0 or lista[i]!=lista[i-1]:
          uusi_lista.append(lista[i])
    return uusi_lista
 
if __name__ == "__main__":
 lista = [3, 2, 2, 1, 3, 3, 1,4,4,4,4,58,2,3,69,2,5,9,7,5,64,66,66,77]
 print(uniikit(lista)) # [1, 2, 3]