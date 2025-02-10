# tee ratkaisu tänne
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!
# tee ratkaisu tänne
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!
 
 
"""
Tee funktio palindromi, joka saa parametriksi merkkijonon ja palauttaa True, jos merkkijono on palindromi (eli samansisältöinen luettuna alusta loppuun tai lopusta alkuun).
 
Tee myös funktiota hyödyntävä pääohjelma, joka kyselee käyttäjältä sanoja niin kauan, kunnes käyttäjä syöttää palindromin:
"""
 
 
"""
print("saippuakauppias on palindromi!") if palindromi("python") else print("ei ollut palindromi")
  print("saippuakauppias on palindromi!") if palindromi("java") else print("ei ollut palindromi")
  print("saippuakauppias on palindromi!") if palindromi("pykauppiasthon") else print("ei ollut palindromi")
  print("saippuakauppias on palindromi!") if palindromi("saippuakauppias") else print("ei ollut palindromi")
"""
 
 
 
def palindromi(lista):
 
    i=0
    j=-1
    check=True
    while i<len(lista):
        if lista[i]!=lista[j]:
            check=False
            #print("ei ollut palindromi")
            return check
             
        i+=1
        j-=1
    if check==True:
        #print(f"{lista } on palindromi!")
        return check    
 
 
 
sana=input("Anna polindromi : ")
while True:
        if palindromi(sana)==True:
            print(f"{sana } on palindromi!")
            break
        else :
            print("ei ollut palindromi")
            sana=input("Anna polindromi : ")
            palindromi(sana)