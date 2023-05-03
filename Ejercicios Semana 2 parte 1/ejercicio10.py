letra = input("Ingrese una letra: ").lower()

if (ord(letra)>=97 and ord(letra)<=122):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("Es una vocal")
    else: 
        print("Es una consonante")
else:
    print("No es una letra del abecedario")