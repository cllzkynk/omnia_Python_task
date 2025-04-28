# tee ratkaisu tänne


def histogrammi(jano):
   
    kirjet={}
    for kirjain in jano:
        kirjain=kirjain.lower()
        if kirjain in kirjet:
            kirjet[kirjain]+=1
        else :
             kirjet[kirjain]=1


    for kirjain , numero in kirjet.items():
        print(kirjain , "*"*numero)


if __name__ == "__main__":
    histogrammi("abba")
    histogrammi("saippuakauppias")









    """
    def histogrammi(merkkijono: str):
    merkit = {}
    for merkki in merkkijono:
        if not merkki in merkit:
            merkit[merkki] = 0
        merkit[merkki] += 1
 
    for merkki, lkm in merkit.items():
        tahdet = "*"*lkm
        print(f"{merkki} {tahdet}")
     # tee ratkaisu tänne
 
   """



