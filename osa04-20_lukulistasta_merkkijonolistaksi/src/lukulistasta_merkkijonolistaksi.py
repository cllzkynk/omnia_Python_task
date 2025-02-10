# tee ratkaisu tänne
 
def muotoile(lista):
    lista2=[]
    for x in lista:
        lista2.append(f"{x:.2f}")
    return lista2
 
 
 
if __name__ == "__main__":
    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)