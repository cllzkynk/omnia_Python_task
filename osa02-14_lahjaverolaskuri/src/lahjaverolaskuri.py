raha = int(input("Lahjan raha: "))
 
if raha < 5000:
    vero = 0
elif raha <= 25000:
    vero = 100 + (raha - 5000) * 0.08
elif raha <= 55000:
    vero = 1700 + (raha - 25000) * 0.10
elif raha <= 200000:
    vero = 4700 + (raha - 55000) * 0.12
elif raha <= 1000000:
    vero = 22100 + (raha - 200000) * 0.15
else:
    vero = 142100 + (raha - 1000000) * 0.17
 
if vero == 0:
    print("Ei veroa!")
else:
    print(f"Vero: {vero} euroa")