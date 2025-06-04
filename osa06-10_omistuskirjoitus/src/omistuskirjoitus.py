def main():
    kenelle = input("Kenelle teos omistetaan: ")
    mihin = input("Mihin kirjoitetaan: ")
    
    teksti = f"Hei {kenelle}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi"
    
 
    with open(mihin, 'w') as tiedosto:
        tiedosto.write(teksti)

main()