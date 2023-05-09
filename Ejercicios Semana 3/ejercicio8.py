text = input("Ingrese un texto o una frase: ")
cant_palabras = 0

for palabra in text.split():
    if palabra.isalpha():
        cant_palabras += 1

print("La cantidad de palabras es: ", cant_palabras)
