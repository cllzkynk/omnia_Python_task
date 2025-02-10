# tee ratkaisu tänne
def positiivisten_summa(lista):
 summa = sum(elementti for elementti in lista if elementti > 0)
 return summa
 
 
 
 
if __name__ == "__main__":
 lista = [1, -2, 3, -4, 5,11]
 vastaus = positiivisten_summa(lista)
 print("vastaus", vastaus)
 