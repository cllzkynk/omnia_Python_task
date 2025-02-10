# Tee ratkaisu tänne
# Tee ratkaisu tänne
 
def anagrammi(str1 , str2):
   lista1=list(str1)
   lista2=list(str2)
   lista1.sort()
   lista2.sort()
  
 
   if lista1==lista2:
      return True
   else : return False
 
 
 
 
if __name__ == "__main__":
   print(anagrammi("talo", "tola")) # True
   print(anagrammi("talor", "lato")) # True
   print(anagrammi("talo", "olat")) # True
   print(anagrammi("tammi", "mitta")) # False
   print(anagrammi("python", "java")) # False
 
 