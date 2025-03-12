"""def kopioi_ja_lisaa(sudoku: list, rivi: int, sarake: int, luku: int):
    uusi = []
    for r in sudoku:
        uusi.append(r[:])
 
    uusi[rivi][sarake] = luku
    return uusi"""







def tulosta(sudoku):
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
 
def kopioi_ja_lisaa(sudoku: list, rivi: int, sarake: int, luku: int):
    container=[]
    for x in range(len(sudoku)):
        container.append([])
     
        for y in range(len(sudoku[x])):
            container[x].append(sudoku[x][y])
        
       
  
    container[rivi][sarake]=luku
    return container 

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

 kopio = kopioi_ja_lisaa(sudoku, 0, 0, 5)
 print("Alkuperäinen:")
 tulosta(sudoku)
 print()
 print("Kopio:")
 tulosta(kopio)


