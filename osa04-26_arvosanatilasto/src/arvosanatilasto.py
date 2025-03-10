
pisteet = []
arvosanat = [0, 0, 0, 0, 0, 0]

while True:
        syote = input("Koepisteet ja harjoitusten määrä: ")
        if syote == "":
            break

        osat = syote.split()
        if len(osat) < 2:
            print("Laita molemmat koepisteet ja harjoitusten määrä.")
            continue

        koepisteet = int(osat[0])
        harjoitukset = int(osat[1])
        harjoituspisteet = harjoitukset // 10
        kokonaispisteet = koepisteet + harjoituspisteet

        if koepisteet < 10:
            arvosana = 0
        elif kokonaispisteet <= 14:
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

        pisteet.append(kokonaispisteet)
        arvosanat[arvosana] += 1

if len(pisteet) > 0:
        keskiarvo = sum(pisteet) / len(pisteet)
        hyväksytyt = sum(arvosanat[1:])
        hyväksymisprosentti = (hyväksytyt / len(pisteet)) * 100

        print("Tilasto:")
        print("Pisteiden keskiarvo:", round(keskiarvo, 1))
        print("Hyväksymisprosentti:", round(hyväksymisprosentti, 1))
        print("Arvosanajakauma:")
        for i in range(5, -1, -1):
            print(f"{i}: {'*' * arvosanat[i]}")
else:
        print("Ei syötettyjä pisteitä.")


