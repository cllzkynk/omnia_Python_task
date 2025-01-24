# Kirjoita ratkaisu tähän
lampotila=float(input("Kerro huominen sääennuste: "))
satavetta=input("Sataako (kyllä/ei): ")

if lampotila>20:
    print(f"Pue housut ja t-paita ")
    if satavetta=="kyllä":
        print("Muista sateenvarjo!")
elif lampotila>10 :
    print("Pue housut ja t-paita\nOta myös pitkähihainen paita")
    if satavetta=="kyllä":
        print("Muista sateenvarjo!")
elif lampotila>5 :
    print("Pue housut ja t-paita\nOta myös pitkähihainen paita\nPue päälle takki")
    if satavetta=="kyllä":
        print("Muista sateenvarjo!")
elif lampotila>0 :
    print("Pue housut ja t-paita\nOta myös pitkähihainen paita\nPue päälle takki\nSuosittelen lämmintä takkia\nKannattaa ottaa myös hanskat")
    if satavetta=="kyllä":
        print("Muista sateenvarjo!")