# Kirjoita ratkaisu tähän
salasana1=input("Kirja salasana: ")

salasana_flag=" "

while salasana1!=salasana_flag:
    salasana_flag=input("Toista salasana: ")
    if salasana1==salasana_flag:
        print("Käyttäjätunnus luotu!")
    else :
     print("Ei ollut sama!")
