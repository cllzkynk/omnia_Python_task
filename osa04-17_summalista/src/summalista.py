# tee ratkaisu tänne
# tee ratkaisu tänne
 
 
def summa(a,b):
 i=0
 summa=[]
 while i<len(a):
  summa.append(a[i]+b[i])
  i+=1
 return summa
 
 
 
if __name__ == "__main__":
 a = [1, 2, 3]
 b = [7, 8, 9]
 print(summa(a, b))
 