# tee ratkaisu tänne


def rivi_oikein(list , num):
    flag=True
   
    for luku in list[num]:
        count1=0
        if luku!=0:
            count1=list[num].count(luku)
   
        if count1>1 or luku>9 or luku<0:
         flag=False
             
    return flag        






if __name__ == "__main__":
 sudoku=[[9, 0, 0, 0, 8, 0, 3, 0, 0],
      [2, 0, 0, 2, 5, 0, 7, 0, 0],
      [0, 2, 0, 3, 0, 0, 0, 0, 4],
      [2, 9, 4, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 7, 3, 0, 5, 6, 0],
      [7, 0, 5, 0, 6, 0, 4, 0, 0],
      [0, 0, 7, 8, 0, 3, 9, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 3],
      [3, 0, 0, 0, 0, 0, 0, 0, 2]]
 print(rivi_oikein(sudoku,1))