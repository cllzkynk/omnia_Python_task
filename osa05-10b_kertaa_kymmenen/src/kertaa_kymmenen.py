# tee ratkaisu tänne



def kertaa_kymmenen(alkuu:int , loppu:int):
 dic={}
 
 for n in range(alkuu,loppu+1):
   dic.update({n:n*10})
 return dic





if __name__ == "__main__":
 d = kertaa_kymmenen(1, 3)
 print(d)


 """def kertaa_kymmenen(alku: int, loppu: int):
    luvut = {}
    for i in range(alku, loppu + 1):
        luvut[i] = i * 10
    return luvut
    # tee ratkaisu tänne"""