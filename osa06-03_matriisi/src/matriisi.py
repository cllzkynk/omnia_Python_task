def lue_matriisi():
  
  matriisi = []
  with open("matriisi.txt") as tiedosto:
      for rivi in tiedosto:
        luvut_str = rivi.strip().split(",")
        rivi_luvut = []
        for luku_str in luvut_str:
          
            rivi_luvut.append(int(luku_str))
        
        if rivi_luvut:
          matriisi.append(rivi_luvut)

  return matriisi

def summa():
  matriisi=lue_matriisi()
  summa = 0
  for rivi in matriisi:
    for luku in rivi:
      summa = summa + luku
  return summa

def maksimi():
  matriisi=lue_matriisi()  
  if not matriisi:
    return None
  maksimi = matriisi[0][0]
  for rivi in matriisi:
    for luku in rivi:
      if luku > maksimi:
        maksimi = luku
  return maksimi

def rivisummat():
  matriisi=lue_matriisi()
  rivisummat = []
  for rivi in matriisi:
    rivisumma = 0
    for luku in rivi:
      rivisumma = rivisumma + luku
    rivisummat.append(rivisumma)
  return rivisummat

if __name__ == "__main__":
  mat = lue_matriisi()
  if mat:
    kokonais_summa = summa()
    suurin_arvo =maksimi()
    rivit_summat = rivisummat()
    print(f"Matriisin summa: {kokonais_summa}")
    print(f"Matriisin suurin alkio: {suurin_arvo}")
    print(f"Rivien summat: {rivit_summat}")
    print(lue_matriisi()[0])