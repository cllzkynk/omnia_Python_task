# tee ratkaisu tänne

def lukukirja():
 sanasto={}
 yksikot=["nolla","yksi","kaksi","kolme","neljä","viisi","kuusi","seitsemän","kahdeksan","yhdeksän"]
 
 
 
 for i in range(100):
  if i<10 :
   sanasto[i]=yksikot[i]
  elif i==10:
   sanasto[i]="kymmenen"
  elif 10<i<20: 
   sanasto[i]=f"{yksikot[i%10]}toista"
  elif 20<i<99 or i==99 or i==20 : 
    if i%10==0:
     sanasto[i]=f"{yksikot[i//10]}kymmentä"
    else:
      sanasto[i]=f"{yksikot[i//10]}kymmentä{yksikot[i%10]}"
 print(f"{sanasto}\n")
 return sanasto




if __name__ == "__main__":
 luvut = lukukirja()
 print(luvut[2])
 print(luvut[11])
 print(luvut[45])
 print(luvut[99])
 print(luvut[0])
 print(luvut[20])
 """
 def lukukirja():
    # Apusanakirja
    ykkoset = {0:"nolla", 1:"yksi", 2:"kaksi", 3:"kolme", 4:"neljä", 5:"viisi", 6:"kuusi", 7:"seitsemän", 8:"kahdeksan", 9:"yhdeksän"}
 
    luvut = {}
 
    # 0 - 9
    for i in range(10):
        luvut[i] = ykkoset[i]
 
    # 10 on erikoistapaus
    luvut[10] = "kymmenen"
 
    # 11 - 19
    for i in range(1, 10):
        luvut[i + 10] = ykkoset[i] + "toista"
 
    # 20 - 99
    for i in range(2, 10):
        luvut[i * 10] = ykkoset[i] + "kymmentä"
        for j in range(1, 10):
            luvut[i * 10 + j] = ykkoset[i] + "kymmentä" + ykkoset[j]
 
    return luvut
 
if __name__ == "__main__":
    print(lukukirja())
# tee ratkaisu tänne
 """