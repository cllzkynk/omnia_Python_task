 
tiedosto = open("paivakirja.txt", "r")
merkinnat = tiedosto.readlines()


while True:
    print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
    valinta = input("Valinta: ")

    if valinta == "0":
        print("Heippa!")
        break
        
    if valinta == "1":
        uusi = input("Anna merkintä: ")
        merkinnat.append(uusi + "\n")
        
        tiedosto = open("paivakirja.txt", "w")
        tiedosto.writelines(merkinnat)
        tiedosto.close()
        
        print("Päiväkirja tallennettu")
        
    if valinta == "2":
        print("Merkinnät:")
        for m in merkinnat:
            print(m.strip())