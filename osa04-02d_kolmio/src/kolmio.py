# kopioi edellisestä tehtävästä funktion viiva koodi tänne
# kopioi edellisestä tehtävästä funktion viiva koodi tänne
 
def viiva(koko, merkki):
  if merkki=="":
    merkki="*"
 
  print(merkki[0]*koko)
 
 
 
 
def kolmio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    kerta=1
    while kerta<=koko:
     viiva(kerta,"#")
     kerta+=1
 
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(2)
 