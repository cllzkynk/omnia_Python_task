# Kirjoita ratkaisu tähän
num1=int(input("Anna num1: "))
num2=int(input("Anna num2: "))
komento=input("Mitä sina haluat ?\n Kirja summa , tulo tai erotus")


#komento=input("Summan varten +  \nminus varten- \nkortous varten x \n")

if komento=="summa" :
    print(f"{num1} + {num2} = {num1+num2}")
elif komento=="tulo" :
    print(f"{num1} * {num2} = {num1*num2}")
elif komento=="erotus" :
    print(f"{num1} - {num2} = {num1-num2}")