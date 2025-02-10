# tee ratkaisu tänne
# tee ratkaisu tänne
 
def kaikki_vaarinpain(lista):
    lista2=[]
    for x in lista:
       lista2.append(x[::-1])
  
    return lista2[::-1]
 
 
 
 
 
if __name__ == "__main__":
    lista = ['abc', 'def']
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)