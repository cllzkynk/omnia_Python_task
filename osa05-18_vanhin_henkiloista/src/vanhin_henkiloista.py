# tee ratkaisu tänne

def vanhin(henkilot: list):
  if not henkilot:
    return ""  

  vanhin_nimi = ""
  vanhin_vuosi = float('inf')  # Alustetaan suurella arvolla

  for nimi, syntymavuosi in henkilot:
    if syntymavuosi < vanhin_vuosi:
      vanhin_vuosi = syntymavuosi
      vanhin_nimi = nimi

  return vanhin_nimi


if __name__ == "__main__":
 h1 = ("Arto", 1977)
 h2 = ("Einari", 1985)
 h3 = ("Maija", 1953)
 h4 = ("Essi", 1997)
 hlista = [h1, h2, h3, h4]

 print(vanhin(hlista))


 """
 def vanhin(henkilot: list):
    vanhin = henkilot[0]
    for henkilo in henkilot:
        # verrataan vanhimman tunnetun ja vuorossa olevan syntymävuotta
        if henkilo[1] < vanhin[1]:
            vanhin = henkilo
 
    return vanhin[0]
# tee ratkaisu tänne
 
"""