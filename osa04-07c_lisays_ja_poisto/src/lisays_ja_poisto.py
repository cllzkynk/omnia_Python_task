lista=[] 
vastaus=""
 
while vastaus!="x":
    print(f"Lista on nyt {lista}")
    vastaus=input("(l)isää, (p)oista vai e(x)it: ")
    if vastaus=="x":
        print("Moi!")
        break
    if vastaus=="l":
        lista.append(len(lista)+1)
    elif vastaus=="p":
        lista.pop(len(lista)-1)
    