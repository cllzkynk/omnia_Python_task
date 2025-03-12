# tee ratkaisu tänne

def lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
  sudoku[rivi_nro][sarake_nro]=luku
 

def tulosta(sudoku:list):
  line=0
  for x in range(0,9):  
    for y in range(0,9):
      if sudoku[x][y]==0:
        sudoku[x][y]="_"
  for rivi in sudoku:
    print()
    if line==3 or line==6:
      print()
    line+=1
      
    for i in range(len(rivi)):
      if i==3 or i==6:
        print("",rivi[i],end=" ")
      else:
       print(rivi[i],end=" ")




if __name__ == "__main__":
 sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

 tulosta(sudoku)
 lisays(sudoku, 0, 0, 2)
 lisays(sudoku, 1, 2, 7)
 lisays(sudoku, 5, 7, 3)
 print()
 print("Kolme numeroa lisätty:")
 print()
 tulosta(sudoku)




 """def tulosta(sudoku: list):
    r = 0
    for rivi in sudoku:
        s = 0
        for merkki in rivi:
            s += 1
            if merkki == 0:
                merkki = "_"
            m = f"{merkki} "
            if s%3 == 0 and s < 8:
                m += " "
            print(m, end="")
 
        print()
        r += 1
        if r%3 == 0 and r < 8:
            print()
 
def lisays(sudoku: list, rivi: int, sarake: int, luku: int):
    sudoku[rivi][sarake] = luku"""