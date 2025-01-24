# Kirjoita ratkaisu tähän
"""
Saatlik ücreti, çalışılan saat sayısını ve haftanın gününü soran bir program yapın. 
Program, saatlik ücretin iki katı olduğu Pazar günleri dışındaki günlerde saat sayısı ile 
saatlik ücret çarpımı olan bir ücret yazdırır.

Örnek çıktı
Saatlik ücret: 8,5 
Çalışma saatleri: 3 
Haftanın günü: Pazartesi 
Maaş 25,5 euro

Örnek çıktı
Saatlik ücret: 12,5 
Çalışma saatleri: 10 
Haftanın günü: Pazar 
Maaş 250,0 euro
"""

tunti=float(input("Tunti : "))
tuntipalkkaa=float(input("Tuntipalkkaa : "))
paiva=input("Paivä : ")

if paiva=="sunnuntai" :
    print(f"Palkka {tunti*tuntipalkkaa*2} euroa")
else:
    print(f"Palkka {tunti*tuntipalkkaa} euroa")