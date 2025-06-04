# tee ratkaisu tänne

if True:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1"
    tehtavatiedot = "tehtavat1"






with open(f"{opiskelijatiedot}") as tiedosto:

     nimet=[]
     for rivi in tiedosto:
        nimi = rivi.strip().split(",")
   
        nimet.append(nimi)
        
nimet=nimet[1:]


with open(f"{tehtavatiedot}") as tiedosto:
     summa=0
     arvot=[]
     for rivi in tiedosto:
       
        arvo = rivi.strip().split(",")
        
        arvot.append(arvo)

arvot=arvot[1:]


 
name=[]
for nimi in nimet:
   
    
   nimi= nimi[0].split(";")[1]+" "+nimi[0].split(";")[2]

   name.append(nimi)

point=[]
for arvo in arvot:
 
    summa=0
    for v in  arvo[0].split(";")[1:]:
        summa=summa+int(v)
    point.append(summa)
 
for i in range(len(name)):
 print(f"{name[i]} {point[i]}")





 
 """
 opiskelijatiedot = input("opiskelijatiedot: ")
tehtavatiedot = input("tehtävätiedot: ")
 
opiskelijat = {}
with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        opiskelijat[osat[0]] = f"{osat[1]} {osat[2].strip()}"
 
tehtavat = {}
with open(tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        summa = 0
        for i in range(1, 8):
            summa += int(osat[i])
        tehtavat[osat[0]] = summa
 
for nro, nimi in opiskelijat.items():
    print(f"{nimi} {tehtavat[nro]}")
# tee ratkaisu tänne
 
 """