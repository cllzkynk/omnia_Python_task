 


# tee ratkaisu tänne



# tee ratkaisu tänne


def laske_alkiot(m , etsittava_luku: int):
    count=0
    for rivi in m:
      for luku in rivi:
         if luku==etsittava_luku:
            count+=1
    return count




if __name__ == "__main__":
  m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
  print(laske_alkiot(m, 1))





