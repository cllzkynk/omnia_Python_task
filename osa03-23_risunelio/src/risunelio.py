# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti

def risunelio(num):
    luku=num
    while num>0:
      print("#"*luku)
      num-=1



if __name__ == "__main__":
    num=int(input("montako: "))
    risunelio(num)


