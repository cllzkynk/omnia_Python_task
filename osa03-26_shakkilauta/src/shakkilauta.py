# tee ratkaisu tänne

# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
def shakkilauta(num):
    lauta=""
    j=1
    i=1
    while j<=num:
      i=1
      while i<=num:
         if (i+j)%2==0:
            lauta=lauta+"1"
         else:
            lauta=lauta+"0"
         i+=1
      j+=1
      print(lauta)
      lauta=""





if __name__ == "__main__":
    shakkilauta(4)




"""
def shakkilauta(koko):
    i = 0
    while i < koko:
        if i % 2 == 0:
            rivi = "10"*koko
        else:
            rivi = "01"*koko
        # poistetaan rivin lopusta ylimääräiset merkit
        print(rivi[0:koko])
        i += 1
# tee ratkaisu tänne
 

"""