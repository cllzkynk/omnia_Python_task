# tee ratkaisu tänne
def pisimman_pituus(lista):
  pisin=""
  for i in range(0,len(lista)):
  
    if i==0 or len(lista[i])>len(pisin):
      pisin=lista[i]
  return len(pisin)
 
 
 
 
 
 
 
if __name__ == "__main__":
  lista = ['Arto', 'Matti']
 
  tulos = pisimman_pituus(lista)
  print(tulos)