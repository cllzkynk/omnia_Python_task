# Kirjoita ratkaisu tähän
count_neg=0
count_poz=0
sum=0
num=1
while num!=0:
    num=int(input("Anna numero: "))
    sum+=num
    if num==0:
        break
    elif num>0:
       count_poz+=1 
    else : count_neg+=1
print("Syötä kokonaislukuja, 0 lopettaa:")
print(f"Lukuja yhteensä {count_neg+count_poz}")
print(f"Lukujen summa {sum}")
print(f"Lukujen keskiarvo {sum/(count_neg+count_poz)}") if (count_neg+count_poz)!=0 else print("Lukujen keskiarvo: division by zero exception")
print(f"Positiivisia {count_poz}")
print(f"Negatiivisia {count_neg}")

"""
25.01.2025 klo 044 kaikki loppu"""