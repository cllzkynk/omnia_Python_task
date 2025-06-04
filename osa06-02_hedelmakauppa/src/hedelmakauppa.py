# tee ratkaisu tänne

def lue_hedelmat():
        with open("hedelmat.csv") as tiedosto:
         hedelmat_hinnat={}
         for rivi in tiedosto:
            osat = rivi.strip().split(";")
            if len(osat) == 2:
              nimi = osat[0]
              hinta = float(osat[1])
              hedelmat_hinnat[nimi] = hinta
        return hedelmat_hinnat
if __name__ == "__main__":
  hedelmat_sanasto = lue_hedelmat()
  if hedelmat_sanasto:
    print(hedelmat_sanasto)