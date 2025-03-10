# tee ratkaisu tänne


def pisin(jonot ):
 pis=""
 for jono in jonot:
    if len(jono)>len(pis):
     pis=jono

 return pis











if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve","jbrvhrjbgreehnber"]
    print(pisin(jonot))