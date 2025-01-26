# Kirjoita ratkaisu tähän
opiskelija=int(input("Montako opiskelijaa? :"))
ryhmansuuri=int(input("Mikä on ryhmän koko? :"))
 
control=opiskelija//ryhmansuuri
#print(control)



if opiskelija%ryhmansuuri==0:
    print(f"Ryhmien määrä: {opiskelija/ryhmansuuri}")
elif opiskelija%ryhmansuuri!=0 :
    print(f"Ryhmien määrä: {int(control+1)}")