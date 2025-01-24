# Kirjoita ratkaisu tähän
# Otetaan käyttöön neliöjuuri math-moduulista
from math import sqrt

# Huomaa, että neliöjuuren voi laskea myös potenssin avulla:
# sqrt(9) on sama asia kuin 9 ** 0.5

lukua=int(input("Anna a : "))
lukub=int(input("Anna b : "))
lukuc=int(input("Anna c : "))
delta=sqrt(lukub**2-(4*lukua*lukuc))

juur1=((-lukub-delta)/(2*lukua))
juur2=((-lukub+delta)/(2*lukua))

print(f"Juuret ovat {juur1} ja {juur2}")





"""
İkinci dereceden ax²+bx+c denklemini çözen bir program yazın. Programa a, b ve c değerleri verilir ve aşağıdaki formülü kullanarak kökleri (yani çözümleri) hesaplaması gerekir.

x = (-b ± sqrt(b²-4ac))/(2a).

Denklemin iki kökü olduğunu varsayalım, bu durumda yukarıdaki formül işe yarayacaktır.

Örnek çıktı:

Örnek çıktı
Anna a: 1 
Anna b: 2 
Anna c: -8

Kökler 2.0 ve -4.0
"""