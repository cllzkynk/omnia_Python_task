

# Ensin kysy,  tiedostot .
opiskelijat_tiedoston_nimi = input("Anna opiskelijatiedot-tiedoston nimi: ")
tehtavat_tiedoston_nimi = input("Anna tehtavatiedot-tiedoston nimi: ")
koepisteet_tiedoston_nimi = input("Anna koepisteet-tiedoston nimi: ")

# Luon tyhjiä paikat, 
opiskelijoiden_nimet = {}
opiskelijoiden_tehtavapisteet = {}
opiskelijoiden_koepisteiden_summa = {}

# Nyt luen opiskelijatiedot-tiedosto.
opiskelijat_tiedosto = open(opiskelijat_tiedoston_nimi, 'r')
eka_rivi = opiskelijat_tiedosto.readline()
for rivi in opiskelijat_tiedosto:
    osat = rivi.strip().split(';')
    opiskelija_numero = osat[0]
    etunimi = osat[1]
    sukunimi = osat[2]
    opiskelijoiden_nimet[opiskelija_numero] = etunimi + " " + sukunimi


# Sitten lue tehtavatiedot-tiedosto.
tehtavat_tiedosto = open(tehtavat_tiedoston_nimi, 'r')
eka_rivi = tehtavat_tiedosto.readline()
for rivi in tehtavat_tiedosto:
    osat = rivi.strip().split(';')
    opiskelija_numero = osat[0]
    tehtavat = [int(x) for x in osat[1:]]
    tehtyjen_tehtavien_maara = sum(tehtavat)
    harjoituspisteet = 0
    kokonaistehtavia = 40 
    if kokonaistehtavia > 0:
        prosenttiosuus = tehtyjen_tehtavien_maara / kokonaistehtavia
        if prosenttiosuus >= 1.0:
            harjoituspisteet = 10
        elif prosenttiosuus >= 0.9:
            harjoituspisteet = 9
        elif prosenttiosuus >= 0.8:
            harjoituspisteet = 8
        elif prosenttiosuus >= 0.7:
            harjoituspisteet = 7
        elif prosenttiosuus >= 0.6:
            harjoituspisteet = 6
        elif prosenttiosuus >= 0.5:
            harjoituspisteet = 5
        elif prosenttiosuus >= 0.4:
            harjoituspisteet = 4
        elif prosenttiosuus >= 0.3:
            harjoituspisteet = 3
        elif prosenttiosuus >= 0.2:
            harjoituspisteet = 2
        elif prosenttiosuus >= 0.1:
            harjoituspisteet = 1
    opiskelijoiden_tehtavapisteet[opiskelija_numero] = harjoituspisteet


# Seuraava lue koepisteet-tiedosto.
koepisteet_tiedosto = open(koepisteet_tiedoston_nimi, 'r')
eka_rivi = koepisteet_tiedosto.readline()
for rivi in koepisteet_tiedosto:
    osat = rivi.strip().split(';')
    opiskelija_numero = osat[0]
    koepisteet = [int(x) for x in osat[1:]]
    koepisteiden_summa = sum(koepisteet)
    opiskelijoiden_koepisteiden_summa[opiskelija_numero] = koepisteiden_summa


# Nyt laske every opiskelijan kokonaispisteet ja arvosana.
 
for opiskelija_numero in opiskelijoiden_nimet:
    if opiskelija_numero in opiskelijoiden_koepisteiden_summa and opiskelija_numero in opiskelijoiden_tehtavapisteet:
        kokonaispisteet = opiskelijoiden_koepisteiden_summa[opiskelija_numero] + opiskelijoiden_tehtavapisteet[opiskelija_numero]
        arvosana = 0
        if kokonaispisteet <= 14:
            arvosana = 0
        elif kokonaispisteet <= 17:
            arvosana = 1
        elif kokonaispisteet <= 20:
            arvosana = 2
        elif kokonaispisteet <= 23:
            arvosana = 3
        elif kokonaispisteet <= 27:
            arvosana = 4
        else:
            arvosana = 5
        nimi = opiskelijoiden_nimet[opiskelija_numero]
        print(nimi + " " + str(arvosana))
    else:
        nimi = opiskelijoiden_nimet[opiskelija_numero]
        print("Huomautus: Opiskelijan " + nimi + " (" + opiskelija_numero + ") tietoja ei löydy kaikista tiedostoista.")
       