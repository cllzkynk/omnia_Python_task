# tee ratkaisu tänne

def nelio_oikein(sudoku: list, rivi: int, sarake: int):
  
  lukut=[]

  for rivi in sudoku[rivi:rivi+3]:
    for luku in rivi[sarake:sarake+3]:
     lukut.append(luku)

  for luku in lukut:
    if luku > 0 and lukut.count(luku)>1:
     return False

  return True
  


if __name__ == "__main__":
 sudoku = [[9, 0, 0, 0, 8, 0, 3, 0, 0], 
           [2, 0, 0, 2, 5, 0, 7, 0, 0], 
           [0, 2, 0, 3, 0, 0, 0, 0, 4], 
           [2, 9, 4, 0, 0, 0, 4, 0, 0], 
           [0, 0, 0, 7, 3, 0, 5, 6, 0], 
           [7, 0, 5, 0, 6, 0, 4, 0, 0], 
           [0, 0, 7, 8, 0, 3, 9, 0, 0], 
           [0, 0, 1, 0, 0, 0, 0, 0, 3], 
           [3, 0, 1, 0, 0, 8, 0, 0, 2]]
 print(nelio_oikein(sudoku, 0, 0))
 print(nelio_oikein(sudoku, 1, 2))
 print(nelio_oikein(sudoku, 5, 5))


