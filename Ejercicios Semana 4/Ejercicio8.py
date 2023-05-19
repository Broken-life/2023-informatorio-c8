txt = input("Ingrese un texto: ")

def es_palindromo(texto):
    if texto == texto[::-1]:
        return print("Es palíndromo")
    else:
        return print("No es palíndromo")
    
es_palindromo(txt)