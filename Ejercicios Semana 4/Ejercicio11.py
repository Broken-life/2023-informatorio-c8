text = input("Ingrese un texto: ")

def contar_vocales(text):
    vocales = 0
    for i in text:
        if i in "aeiou":
            vocales += 1
    return vocales

contar_vocales(text)
print(f"El texto ingresado tiene {contar_vocales(text)} vocales")