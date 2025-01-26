# Kirjoita ratkaisu tähän
pinkoodi=int(4321)

yritykset =0

while True :
    tunnus = int(input("Anna PIN-koodi: "))
    yritykset+=1

    if pinkoodi==tunnus:
     
        if yritykset==1:
            print(f"Oikein, tarvitsit vain yhden yrityksen!")
        else:
            print(f"Oikein, tarvitsit {yritykset} yritystä")
        break
    else :
        print("Väärin")

