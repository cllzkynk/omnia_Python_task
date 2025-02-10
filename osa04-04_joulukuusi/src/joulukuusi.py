# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
 
def joulukuusi(koko):
    #pitkin rivi koko*2-1
    #bosluk lazim   bosluk koko-1
    #adim lazim  adim koko 
    print("joulukuusi!")
    blank=koko-1
    riivi=1
    while blank>=0:
        print(" "*blank+"*"*riivi+" "*blank)
        riivi+=2
        blank-=1
    print(" "*(koko-1)+"*")
 
 
 
 
 
if __name__ == "__main__":
    joulukuusi(5)