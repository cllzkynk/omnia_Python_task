# tee ratkaisu tänne
def pisin_naapurijono(lista):
    en_uzun = 1
    simdiki_uzunluk = 1

    for i in range(1, len(lista)):
        print(f"adim {i}")
        if abs(lista[i] - lista[i - 1]) == 1:
            simdiki_uzunluk += 1
        else:
            if simdiki_uzunluk > en_uzun:
                en_uzun = simdiki_uzunluk
            simdiki_uzunluk = 1

    if simdiki_uzunluk > en_uzun:
        en_uzun = simdiki_uzunluk
    return  en_uzun
    

if __name__ == "__main__":
 lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
 print(pisin_naapurijono(lista))

 """def pisin_naapurijono(lista: list):
    pisin = 1
    tulos = 1
    for i in range(1, len(lista)):
        # funktio abs laskee itseisarvon
        if abs(lista[i-1]-lista[i]) == 1:
            tulos += 1
        else:
            tulos = 1
        # funktio max antaa suurimman parametreista
        pisin = max(pisin, tulos)
    return pisin
 
# tee ratkaisu tänne"""