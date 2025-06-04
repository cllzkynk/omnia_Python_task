# tee ratkaisu tänne

def lisaa_opiskelija(oppilaat, nimi):

  """
  Lisää uuden oppilaan rekisteriin.
  Oppilaan tiedot alustetaan tyhjiksi.
  """
  if nimi not in oppilaat:
    oppilaat[nimi] = {"suoritukset": []}

def tulosta(oppilaat, nimi):
  
  """
  Tulostaa yhden oppilaan tiedot.
  Jos oppilasta ei löydy, siitä ilmoitetaan.
  """
  if nimi in oppilaat:
    print(f"{nimi}:")
    if not oppilaat[nimi]["suoritukset"]:
      print(" ei suorituksia")
    else:
      print(f" suorituksia {len(oppilaat[nimi]['suoritukset'])} kurssilta:")
      summa = 0
      for suoritus in oppilaat[nimi]["suoritukset"]:
        kurssi = suoritus[0]
        arvosana = suoritus[1]
        print(f"  {kurssi} {arvosana}")
        summa += arvosana
      keskiarvo = summa / len(oppilaat[nimi]["suoritukset"])
      print(f" keskiarvo {keskiarvo}")
  else:
    print(f"ei löytynyt ketään nimellä {nimi}")

def lisaa_suoritus(oppilaat, nimi, suoritus_tuple):
  """
  Lisää oppilaalle uuden kurssisuorituksen.
  Jos arvosana on 0, suoritusta ei lisätä.
  Jos kurssi on jo suoritettu korkeammalla arvosanalla,
  uutta suoritusta ei lisätä.
  """
  if nimi in oppilaat:
    kurssi = suoritus_tuple[0]
    arvosana = suoritus_tuple[1]
    if arvosana > 0:
      on_jo = False
      for i in range(len(oppilaat[nimi]["suoritukset"])):
        if oppilaat[nimi]["suoritukset"][i][0] == kurssi:
          if oppilaat[nimi]["suoritukset"][i][1] < arvosana:
            oppilaat[nimi]["suoritukset"][i] = suoritus_tuple
          on_jo = True
          break
      if not on_jo:
        oppilaat[nimi]["suoritukset"].append(suoritus_tuple)

def kooste(oppilaat):
  """
  Tulostaa koosteen opiskelijoiden suorituksista:
  - opiskelijoiden kokonaismäärä
  - eniten suorituksia tehnyt opiskelija ja suoritusten määrä
  - paras keskiarvo ja sen saavuttanut opiskelija
  """
  opiskelija_lkm = len(oppilaat)
  eniten_suorituksia_lkm = 0
  eniten_suorituksia_nimi = ""
  paras_keskiarvo = -1
  paras_keskiarvo_nimi = ""

  for nimi, tiedot in oppilaat.items():
    suoritusten_maara = len(tiedot["suoritukset"])
    if suoritusten_maara > eniten_suorituksia_lkm:
      eniten_suorituksia_lkm = suoritusten_maara
      eniten_suorituksia_nimi = nimi

    if tiedot["suoritukset"]:
      summa = sum(suoritus[1] for suoritus in tiedot["suoritukset"])
      keskiarvo = summa / suoritusten_maara
      if keskiarvo > paras_keskiarvo:
        paras_keskiarvo = keskiarvo
        paras_keskiarvo_nimi = nimi
    elif opiskelija_lkm == 1 and paras_keskiarvo == -1:
        paras_keskiarvo = 0
        paras_keskiarvo_nimi = nimi


  print(f"opiskelijoita {opiskelija_lkm}")
  if eniten_suorituksia_nimi:
    print(f"eniten suorituksia {eniten_suorituksia_lkm} {eniten_suorituksia_nimi}")
  if paras_keskiarvo_nimi:
    print(f"paras keskiarvo {paras_keskiarvo} {paras_keskiarvo_nimi}")


if __name__ == "__main__":
 opiskelijat = {}
 lisaa_opiskelija(opiskelijat, "Pekka")
 lisaa_opiskelija(opiskelijat, "Liisa")
 tulosta(opiskelijat, "Pekka")
 tulosta(opiskelijat, "Liisa")
 tulosta(opiskelijat, "Jukka")

 lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
 lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
 tulosta(opiskelijat, "Pekka")

 lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 0))
 lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 2))
 tulosta(opiskelijat, "Pekka")
 

 lisaa_opiskelija(opiskelijat, "Jukka")
 lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
 lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
 lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 1))
 lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
 lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
 kooste(opiskelijat)