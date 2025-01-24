# Kirjoita ratkaisu tähän

nimi=input("Anna nimesi: ")
lukumaara=0
annos=float(5.90)
kokohinta=0

if nimi=="Jerry" :
    print("Seuraava!") 
else :
    lukumaara=float(input("Kuinkam monta? :") )
    
    kokohinta=lukumaara*annos
    print(f"Kokonaishinta on {float(kokohinta)}\nSeuraava!")     
