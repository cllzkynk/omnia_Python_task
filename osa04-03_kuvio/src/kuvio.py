# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(5, "x", 2, "o")
# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def viiva(leveys, merkkijono):
  if merkkijono=="":
    merkkijono="*"
 
  print(merkkijono[0]*leveys)
 
 
 
 
 
def kuvio(koko1,merkki1,koko2,merkki2):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    kerta=1
    while kerta<=koko1:
     viiva(kerta,merkki1)
     kerta+=1
    kerta=1
    while kerta<=koko2:
     viiva(koko1,merkki2)
     kerta+=1
 
 
if __name__ == "__main__":
    kuvio(5, "x", 2, "o")
 