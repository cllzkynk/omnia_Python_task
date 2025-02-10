# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
 
def eka_sana(lause):
    separate=lause.rsplit(" ") 
    return separate[0]
 
def toka_sana(lause):
    separate=lause.rsplit(" ") 
    return separate[1] 
 
def vika_sana(lause):
    separate=lause.rsplit(" ")
    return separate[len(separate)-1]
 
 
 
#separate
 
 
if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause))
    print(toka_sana(lause)) 
    print(vika_sana(lause))