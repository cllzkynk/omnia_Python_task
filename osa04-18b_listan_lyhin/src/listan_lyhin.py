# tee ratkaisu tänne
def lyhin(lista):
  lyhin=""
  for i in range(0,len(lista)):
  
    if i==0 or len(lista[i])<len(lyhin):
      lyhin=lista[i]
  return lyhin
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
if __name__ == "__main__":
  lista = ["pekka", "emilia", "johanna", "venla", "eero", "antti","fg"]
 
  tulos = lyhin(lista)
  print(tulos)