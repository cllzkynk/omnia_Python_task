# tee ratkaisu tänne

def ilman_vokaaleja (jono):
 vokaalit=["a","e","o","u","y","ä","å","ö","i"]
 uusi_jono=""
 for i in jono:
  
  if i in vokaalit:
  
   continue
  uusi_jono=uusi_jono+i

 return uusi_jono










if __name__ == "__main__":
 mjono = "tstisn"
 print(ilman_vokaaleja(mjono))