# Kirjoita ratkaisu tähän

sano1=input("Anna ensimäinen sano: ")
sano2=input("Anna toinen sano: ")


if sano1==sano2 :
    print(f"Annoit saman sanan kahdesti.")
elif sano1>sano2:
     print(f"{sano1} on aakkosjärjestyksessä viimeinen.")
else:
     print(f"{sano2} on aakkosjärjestyksessä viimeinen.")