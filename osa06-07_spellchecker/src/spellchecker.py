# tee ratkaisu tänne
# dogru kelimeleri okuyalim 
with open("wordlist.txt", "r") as sanatiedosto:
    oikein_sanat = [sana.strip().lower() for sana in sanatiedosto.readlines()]

# kullanici girisi alalim 
kayttaja_teksti = input("Write text: ")

# kullanicinin yazisini kelimelere parcala
tekstin_sanat = kayttaja_teksti.split()

# kelimeleri kontrol edelim 
tarkistetut_sanat = []
for sana in tekstin_sanat:
    if sana.lower() in oikein_sanat:
        tarkistetut_sanat.append(sana)  # ok
    else:
        tarkistetut_sanat.append(f"*{sana}*")  # wrong

#
print(" ".join(tarkistetut_sanat))