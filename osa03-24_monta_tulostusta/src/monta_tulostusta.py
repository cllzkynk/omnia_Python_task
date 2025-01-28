# tee ratkaisu tähän
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def tulosta_monesti(viesti, kerta):
    while kerta>0:
     print(viesti)
     kerta-=1

if __name__ == "__main__":
    
    tulosta_monesti("Ali", 3)