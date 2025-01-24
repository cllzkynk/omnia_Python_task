# Kirjoita ratkaisu tähän

piste=float(input("Anna pisteet [0-100]: "))

if piste<0:
    print("mahdotonta!")
elif piste>=0 and piste<=49:
    print("hylätty")
elif piste>=50 and piste<=59:
    print("Arvosana: 1")
elif piste>=60 and piste<=69:
    print("Arvosana: 2")
elif piste>=70 and piste<=79:
    print("Arvosana: 3")
elif piste>=80 and piste<=89:
    print("Arvosana: 4")
elif piste>=90 and piste<=100:
    print("Arvosana: 5")
else:print("mahdotonta!")
