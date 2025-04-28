# tee ratkaisu tänne





def transponoi(matriisi: list):



   rivi_maara=len(matriisi)
   sarake_maara=len(matriisi[0]) if rivi_maara>0 else 0
   
   transponoitu_matriisi=[]
   for j in range(sarake_maara):
     uusi_rivi=[]
     for i in range(rivi_maara):
       
       uusi_rivi.append(matriisi[i][j])
     transponoitu_matriisi.append(uusi_rivi)
   x=len(matriisi)
   y=len(matriisi[0]) if x>0 else 0
   for i in range(x):
      
     for j in range(y):
        matriisi[i][j]=transponoitu_matriisi[i][j]


if __name__ == "__main__":
 #matriisi= [[1,2,3],[4,5,6],  [7,8,9]]
 matriisi=[[10, 100], 
           [10, 100]] 
 transponoi(matriisi)
 print(matriisi)
#kfjb
 """Teachers solution
 def transponoi(matriisi: list):
    n = len(matriisi)
    for i in range(n):
        for j in range(i, n):
            temp = matriisi[i][j]
            matriisi[i][j] = matriisi[j][i]
            matriisi[j][i] = temp
 
            #..tai vaihtoehtoisesti
            # matriisi[i][j], matriisi[j][i] = matriisi[j][i], matriisi[i][j]"""
            # dvdvdvd
