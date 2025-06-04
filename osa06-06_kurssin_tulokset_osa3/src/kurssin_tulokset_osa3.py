 
opiskelijat_tiedosto = input("Opiskelijatiedot-tiedosto: ")
tehtavat_tiedosto = input("Tehtavatiedot-tiedosto: ")
koepisteet_tiedosto = input("Koepisteet-tiedosto: ")

opiskelijoiden_nimet = {}
opiskelijoiden_tehtavat = {}
opiskelijoiden_koepisteet = {}

# Lue opiskelijatiedot-tiedosto 
with open(opiskelijat_tiedosto, 'r') as file:
    eka_rivi = file.readline()
    for line in file:
        osat = line.strip().split(';')
        opiskelijanumero = osat[0]
        etunimi = osat[1]
        sukunimi = osat[2]
        opiskelijoiden_nimet[opiskelijanumero] = etunimi + " " + sukunimi


with open(tehtavat_tiedosto, 'r') as file:
    eka_rivi = file.readline()
    for line in file:
        osat = line.strip().split(';')
        opiskelijanumero = osat[0]
        tehtavat = [int(x) for x in osat[1:]]
        opiskelijoiden_tehtavat[opiskelijanumero] = sum(tehtavat)

with open(koepisteet_tiedosto, 'r') as file:
    eka_rivi = file.readline()
    for line in file:
        osat = line.strip().split(';')
        opiskelijanumero = osat[0]
        pisteet = [int(x) for x in osat[1:]]
        opiskelijoiden_koepisteet[opiskelijanumero] = sum(pisteet)

print(f"{'nimi':<30}{'teht_lkm':<10}{'teht_pist':<10}{'koe_pist':<10}{'yht_pist':<10}{'arvosana':<10}")

for numero, nimi in opiskelijoiden_nimet.items():
    tehtavat_lkm = opiskelijoiden_tehtavat.get(numero, 0)
    koe_piste = opiskelijoiden_koepisteet.get(numero, 0)

    tehtava_piste = 0
    if 0 <= tehtavat_lkm <= 3:
        tehtava_piste = 0
    elif 4 <= tehtavat_lkm <= 7:
        tehtava_piste = 1
    elif 8 <= tehtavat_lkm <= 11:
        tehtava_piste = 2
    elif 12 <= tehtavat_lkm <= 15:
        tehtava_piste = 3
    elif 16 <= tehtavat_lkm <= 19:
        tehtava_piste = 4
    elif 20 <= tehtavat_lkm <= 23:
        tehtava_piste = 5
    elif 24 <= tehtavat_lkm <= 27:
        tehtava_piste = 6
    elif 28 <= tehtavat_lkm <= 31:
        tehtava_piste = 7
    elif 32 <= tehtavat_lkm <= 35:
        tehtava_piste = 8
    elif 36 <= tehtavat_lkm <= 38:
        tehtava_piste = 9
    elif tehtavat_lkm == 39 or tehtavat_lkm == 40:
        tehtava_piste = 10

    yhteispisteet = koe_piste + tehtava_piste
    arvosana = 0
    if yhteispisteet <= 14:
        arvosana = 0
    elif yhteispisteet <= 17:
        arvosana = 1
    elif yhteispisteet <= 20:
        arvosana = 2
    elif yhteispisteet <= 23:
        arvosana = 3
    elif yhteispisteet <= 27:
        arvosana = 4
    else:
        arvosana = 5

  
    print(f"{nimi:<29} {tehtavat_lkm:<10}{tehtava_piste:<10}{koe_piste:<10}{yhteispisteet:<10}{arvosana:<10}")


    