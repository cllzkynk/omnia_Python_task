# Kirjoita ratkaisu tähän
tarina=""
sanacontrol=""
while True:
    sana=input("Anna sana: ")
    if sana=="loppu" or sana==sanacontrol:
        break
    tarina=tarina+sana+ " "
    sanacontrol=sana
print(tarina)