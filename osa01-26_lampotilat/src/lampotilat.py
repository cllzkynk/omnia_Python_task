# Kirjoita ratkaisu tähän

fahrnt=input("Anna lämpötila (F): ")
#°C = (°F - 32) ÷ (9/5)
celcius =(int(fahrnt)-32)/(9/5)


if celcius<0 :
    print(f"{fahrnt} fahrenheit-astetta on {celcius} celsius-astetta\nPaleltaa!")
else:
    print(f"{fahrnt} fahrenheit-astetta on {celcius} celsius-astetta")



"""
Anna lämpötila (F): 101
101 fahrenheit-astetta on 38.333333333333336 celsius-astetta

Anna lämpötila (F): 21
21 fahrenheit-astetta on -6.111111111111111 celsius-astetta
Paleltaa!

"""
