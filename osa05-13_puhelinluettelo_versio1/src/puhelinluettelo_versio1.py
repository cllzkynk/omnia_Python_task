# tee ratkaisu tänne


Puhelinluettelo={}
while True:
       komento=int(input("komento (1 hae, 2 lisää, 3 lopeta): "))
       if komento==1:
          kuka=str(input("Nimi : "))
          print(Puhelinluettelo.get(kuka,"ei numeroa"))
           
       if komento==2:
           kuka=str(input("Nimi : "))
           numero=str(input("Numero: "))
           Puhelinluettelo[kuka]=numero
           print("ok!")
       if komento==3:
        print("lopetetaan...")
        break


"""
def hae(henkilot):
    nimi = input("nimi: ")
    if nimi in henkilot:
        print(henkilot[nimi])
    else:
        print("ei numeroa")
 
def lisaa(henkilot):
    nimi = input("nimi: ")
    numero = input("numero: ")
    henkilot[nimi] = numero
    print("ok!")
 
def main():
    henkilot = {}
    while True:
        komento = input("komento (1 hae, 2 lisää, 3 lopeta): ")
        if komento == "1":
            hae(henkilot)
        if komento == "2":
            lisaa(henkilot)
        if komento == "3":
            break
    print("lopetetaan...")
 
main()
"""

