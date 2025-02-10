# Kirjoita ratkaisu tähän
sanat=[]
 
while True:
    sana=input("sana: ")
    if sana in sanat:
        print(f"Annoit {len(sanat)} eri sanaa")
        break
    else :
        sanat.append(sana)