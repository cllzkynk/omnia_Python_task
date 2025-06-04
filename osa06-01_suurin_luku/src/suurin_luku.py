# tee ratkaisu tänne
def suurin():
    
    with open("luvut.txt") as tiedosto:
     ehdo=float("-inf")
     for rivi in tiedosto:
        luku=int(rivi.strip())
        if luku>ehdo:
            ehdo=luku
    return ehdo
   
if __name__ == "__main__":
  print(suurin())
  