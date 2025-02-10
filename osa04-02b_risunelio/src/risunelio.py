def viiva(koko, merkkijono):
  if merkkijono=="":
    merkkijono="*"
 
  print(merkkijono[0]*koko)
 
 
def risunelio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    kerta=koko
    while kerta>0:
     viiva(koko, "#")
     kerta-=1
 
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
 