# tee ratkaisu tänne

"""
def etsi_elokuvat(rekisteri: list, hakusana: str):
    loydetyt = []
    for elokuva in rekisteri:
        # Funktio lower() muuntaa merkkijonon pieniksi kirjaimiksi
        # Kun tämä tehdään molemmille merkkijonoille, kirjainkokojen
        # merkitys katoaa
        if hakusana.lower() in elokuva["nimi"].lower():
            loydetyt.append(elokuva)
 
    return loydetyt
# tee ratkaisu tänne
 
"""

 

def etsi_elokuvat(rekisteri, hakusana):
   tulokset=[]
   hakuasana_lower=hakusana.lower()
   for elokuva in rekisteri:
     nimi_lower=elokuva.get("nimi","").lower()
     ohjaaja_lower=elokuva.get("ohjaaja","").lower()
     if hakuasana_lower in ohjaaja_lower or hakuasana_lower in nimi_lower:
       tulokset.append(elokuva)
   return tulokset












if __name__ == "__main__":
 rekisteri = []
 rekisteri = [{"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116},
 {"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pythonen", "vuosi": 2001, "pituus": 94},
 {"nimi": "Koodaajien yö", "ohjaaja": "M. Night Python", "vuosi": 2011, "pituus": 101}]

 lista = etsi_elokuvat(rekisteri, "python")
 print(lista)