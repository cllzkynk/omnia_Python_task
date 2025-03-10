# tee ratkaisu tänne
def poista_isot(lista):
 uusi_lista=[]
 for i in lista:
  if i.isupper():
   continue
  uusi_lista.append(i)

 return uusi_lista




if __name__ == "__main__":
 lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
 karsittu_lista = poista_isot(lista)
 print(karsittu_lista)

# command 
 """
def poista_isot(merkkijonot: list):
    ilman_isoja = []
 
    for merkkijono in merkkijonot:
        if not merkkijono.isupper():
            ilman_isoja.append(merkkijono)
 
    return ilman_isoja
# tee ratkaisu tänne
 
 """