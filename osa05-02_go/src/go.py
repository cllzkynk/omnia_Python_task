# tee ratkaisu tänne



def kumpi_voitti(pelilauta):
    player1=0
    player2=0
    for rivi in pelilauta:
        for piste in rivi:
            if piste==1:
                player1+=1
            elif piste==2:
                player2+=1
    if player1>player2:
        return 1
    elif player2>player1:
        return 2
    else:
        return 0





if __name__ == "__main__":
   

    print(kumpi_voitti(pelilauta = [
  [1, 0, 1, 2, 0, 1, 0, 2, 0],
  [2, 0, 1, 2, 1, 0, 0, 0, 0],
  [0, 0, 1, 2, 0, 1, 0, 2, 0],
  [0, 1, 0, 0, 0, 0, 2, 2, 0],
  [0, 0, 0, 2, 0, 1, 0, 0, 0],
  [0, 2, 0, 1, 0, 0, 2, 2, 0],
  [0, 2, 0, 0, 2, 0, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 2, 0],
  [0, 0, 1, 0, 2, 1, 0, 1, 0]]))
    