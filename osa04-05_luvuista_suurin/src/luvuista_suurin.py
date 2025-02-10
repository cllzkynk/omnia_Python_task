# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def luvuista_suurin(a, b, c):
     if a >= b and a >= c:
        return a
     elif b >= c:
        return b
     else:
        return c
 
 
 
 
 
 
 
if __name__ == "__main__":
    suurin = luvuista_suurin(1, 8, 8)
    print(suurin)