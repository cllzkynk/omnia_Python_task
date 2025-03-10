def sudoku_oikein(sudoku: list):
   if rivi_oikein(sudoku)==True and sarake_oikein(sudoku)==True and nelio_oikein(sudoku)==True:
     return True
   else:
      return False

def nelio_oikein(sudoku: list):
  lukut=[]
  for x in [0,3,6]:
    for y  in [0,3,6]:
         
        lukut=[]
        for rivi in sudoku[x:x+3]:
            for luku in rivi[y:y+3]:
                 lukut.append(luku)
                
        for luku in lukut:
          if luku > 0 and lukut.count(luku)>1:
            
           return False

  return True   
        
def sarake_oikein(sudoku: list ):
    list_varasto=[]
    for i in range(0,len(sudoku)):
       
      list_varasto=[]
      for rivi in sudoku:
       
       list_varasto.append(rivi[i])
       
       count1=0
       if rivi[i]!=0:
        count1=list_varasto.count(rivi[i])
       
       
       if count1>1 or rivi[i]>9 or rivi[i]<0:
         
         return False
    return True
    
def rivi_oikein(sudoku: list):
   i=0
   for luku in sudoku[i]:
        
        count1=0
        if luku!=0:
            count1=sudoku[i].count(luku)
   
        if count1>1 or luku>9 or luku<0:
         return False
         break
        i+=1 
        if i>9:
          break
        return True  


if __name__ == "__main__":
 sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]

 print(sudoku_oikein(sudoku1))

 sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]]

 print(sudoku_oikein(sudoku2))