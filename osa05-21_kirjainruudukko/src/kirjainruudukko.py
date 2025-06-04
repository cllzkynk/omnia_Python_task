
kerrosluku = int(input("Kerrokset: "))
koko = kerrosluku * 2 - 1
kirjaimet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ruudukko = []

for i in range(koko):
    rivi = ""
    for j in range(koko):
      keski = kerrosluku - 1
      i_ero = abs(i - keski)
      j_ero = abs(j - keski)
      suurin_ero = max(i_ero, j_ero)
      kirjain_indeksi = suurin_ero
      rivi = rivi + kirjaimet[kirjain_indeksi]
    ruudukko.append(rivi)

for rivi in ruudukko:
    print(rivi)


