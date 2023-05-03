char = input("Ingrese un caracter: ")
caracter = ord(char)

if caracter >= 65 and caracter <= 90:
    print("El caracter ingresado es una letra mayuscula.")
elif caracter >= 97 and caracter <= 122:
    print("El caracter ingresado es una letra minuscula.")
elif caracter >= 48 and caracter <= 57:
    print("El caracter ingresado es un numero.")
else:
    print("El caracter ingresado es un simbolo.")


#utilizando el coddigo ASCII
#la funcion ord() devuelve el numero dominal que representa el caracter.
#https://elcodigoascii.com.ar
