# Kirjoita ratkaisu tähän
kirje1=input("Anna 1. kirjain: ")
kirje2=input("Anna 2. kirjain: ")
kirje3=input("Anna 3. kirjain: ")

if (kirje1<kirje2 and kirje1>kirje3)or(kirje1<kirje3 and kirje1>kirje2):
    print(f"Keskimmäinen kirjain on {kirje1}")
elif (kirje2<kirje1 and kirje2>kirje3)or(kirje2<kirje3 and kirje2>kirje1):
    print(f"Keskimmäinen kirjain on {kirje2}")
else:print(f"Keskimmäinen kirjain on {kirje3}")


"""
Anna 1. kirjain: x
Anna 2. kirjain: c
Anna 3. kirjain: p
Keskimmäinen kirjain on p
"""
