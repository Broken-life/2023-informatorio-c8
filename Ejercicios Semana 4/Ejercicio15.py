txt = input("Ingrese un texto: ")

def contar_palabras(txt):
    palabras = txt.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras

print(f"La cantidad de palabras es: {contar_palabras(txt)}")