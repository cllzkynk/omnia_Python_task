# tee ratkaisu tänne
def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
  if 0<=x and x<=2 and 0<=y and y<=2 :
   if lauta[y][x]=="":
    lauta[y][x]=nappula 
    return True
   else:
    return False
  else:
   #print("x and y must be 0 and 2 between")
   return False

if __name__ == "__main__":
 lauta = [["", "x", "x"],
          ["", "x", ""], 
          ["o", "x", ""]]
 print(pelaa_siirto(lauta, 0, 0, "X"))
 print(lauta)