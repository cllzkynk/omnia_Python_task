# tee ratkaisu tänne
def parilliset(lista):
 
 i=0
 uusi_lista=[]
 
 while i<len(lista):
  if lista[i]%2==0:
   uusi_lista.append(lista[i]) 
  i+=1
 return uusi_lista
 
 
 
 
 
if __name__ == "__main__":
 lista = [1, 2, 3, 4, 5,11,16,18,23,21,32]
 uusi_lista=parilliset(lista)
 print("alkuperäinen", lista)
 print("uusi", uusi_lista)