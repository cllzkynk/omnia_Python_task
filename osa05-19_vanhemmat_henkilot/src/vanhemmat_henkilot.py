# tee ratkaisu tänne

def vanhemmat(henkilot_lista, raja_vuosi):
     vanhemmat_nimet = []
     for henkilö in henkilot_lista:
      nimi = henkilö[0]
      syntymävuosi = henkilö[1]
      if syntymävuosi < raja_vuosi:
       vanhemmat_nimet.append(nimi)
     return vanhemmat_nimet

 

if __name__ == "__main__":
 h1 = ("Arto", 1977)
 h2 = ("Einari", 1985)
 h3 = ("Maija", 1953)
 h4 = ("Essi", 1997)
 hlista = [h1, h2, h3, h4]

 vanhemmat_henkilot = vanhemmat(hlista, 1979)
 print(vanhemmat_henkilot)