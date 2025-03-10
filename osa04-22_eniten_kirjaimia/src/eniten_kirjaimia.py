# tee ratkaisu tänne



import re

def eniten_kirjainta(jono):
  count=0
  lista=re.findall('.',jono)
  ehto=""
  #print( lista)
  for i in lista:
    if jono.count(i)>count:
     count=jono.count(i)
     ehto=i

  return ehto



if __name__ == "__main__":
  mjono = "esimerkkimerkkijonokki"
  print(eniten_kirjainta(mjono))