# Kirjoita ratkaisu tähän

print("Henkilö 1:")
nimi1=input("Anna nimesi: ")
ika1=int(input("Anna ikäsi: "))

print("Henkilö 2:")
nimi2=input("Anna nimesi: ")
ika2=int(input("Anna ikäsi: "))

if ika1==ika2 :
    print(f"{nimi1} ja {nimi2} ovat yhtä vanhoja")
elif ika1>ika2:
     print(f"Vanhempi on {nimi1}")
else:
    print(f"Vanhempi on {nimi2}")