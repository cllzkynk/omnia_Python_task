from math import sqrt

while True:
    luku=float(input("Anna luku : "))
    if luku==0:
        print("Lopetetaan...")
        break
    elif luku>0:
        print(sqrt(luku))
    else:
        print("Epäkelpo luku")

    

