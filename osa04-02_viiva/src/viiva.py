# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def viiva(leveys, merkkijono):
  if merkkijono=="":
    merkkijono="*"
 
  print(merkkijono[0]*leveys)
 
 
 
 
 
if __name__ == "__main__":
    viiva(5, "")
 