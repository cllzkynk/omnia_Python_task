# tee ratkaisu tänne
def  pisimmat(lista):
    uusi_lista=[]
   
 
    for i in range(len(lista)):
      
       if i==0 or len(lista[i])==len(uusi_lista[0]):
          uusi_lista.append(lista[i])
       if len(lista[i])>len(uusi_lista[0]):
          uusi_lista.clear()
          uusi_lista.append(lista[i])
       print(uusi_lista)
 
 
    return uusi_lista
 
 
 
 
 
 
 
 
 
if __name__ == "__main__":
 lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
 
 tulos = pisimmat(lista)
 print(tulos) # ['emilia', 'juhani']