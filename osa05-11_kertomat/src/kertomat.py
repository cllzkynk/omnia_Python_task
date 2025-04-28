import math

# tee ratkaisu tänne

def kertomat(n: int):
 faktoriyel={}
 
 for r in range(1,n+1):
  

  faktoriyel.update({r:math.factorial(r)})
  
 return faktoriyel

if __name__ == "__main__":
 k = kertomat(1)
 print(k)
 print(k[1])


