# Kirjoita ratkaisu tähän

sy=int(input("Montako kertaa viikossa syöt Unicafessa?: "))
sy_hinta=float(input("Unicafe-lounaan hinta?: "))
osto_ruoka=float(input("Paljonko käytät viikossa ruokaostoksiin?: "))
vikonsyomene=sy*sy_hinta
vikonkaikimene=osto_ruoka+vikonsyomene

print(f"Kustannukset keskimäärin:\n Päivässä {vikonkaikimene/7} euroa\nViikossa {vikonkaikimene} euroa")
