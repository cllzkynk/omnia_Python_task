# tee ratkaisu tänne
# tee ratkaisu tänne


def sarake_oikein(list , num):
    flag=True
    list_varasto=[]
    for rivi in list:
     
       list_varasto.append(rivi[num])
       count1=0
       if rivi[num]!=0:
        count1=list_varasto.count(rivi[num])
            
       if count1>1 or rivi[num]>9 or rivi[num]<0:
         
         flag=False
         break



    return flag        






if __name__ == "__main__":
 sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [2, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [11, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]
 print(sarake_oikein(sudoku,0))