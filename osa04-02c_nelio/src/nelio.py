def viiva(koko, merkki):
  if merkki=="":
    merkki="*"
 
  print(merkki[0]*koko)
 
 
 
 
def nelio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    kerta=koko
    while kerta>0:
     viiva(koko,merkki)
     kerta-=1
 
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(3, "o")
 