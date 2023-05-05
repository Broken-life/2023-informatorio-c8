frase = str(input("Ingrese una frase, palabra, o texto:").lower()) #pasamos todo a minuscula

#eliminar los signos de puntuacion de la frase con un map, para dejar solo letra
# signos = [",", ".", ";", ":", "¿", "?", "¡", "!", "(", ")", '"', "'"]
# frase2 = list(map(lambda x: x if x not in signos else " ", frase))
# frase2 = "".join(frase2)
# print(frase)

letra_1 = str(input("Ingrese una letra: "))
letra_2 = str(input("Ingrese otra letra: "))
letra_3 = str(input("Ingrese otra letra: "))

#metemos las letras en una lista
letras = [letra_1.lower(), letra_2.lower(), letra_3.lower()]

#cantidad de veces que aparece cada letra elegida en el texto ingresado
for letra in letras:
    frase.count(letra) 
    print(f"La letra {letra} aparece {frase.count(letra)} veces en la frase")

#cantidad de palabras que tiene la frase ingresada
frase.split()
print(f"La frase tiene {len(frase.split())} palabra/s")

#primera letra y ultima letra de la frase ingresada
print(f"La primera letra de la frase es {frase[0]} y la ultima letra es {frase[-1]}")

#mostrar el texto ingresado, en orden inverso
print(f"El texto ingresado en orden inverso es {frase[::-1]}")

#verificar si la palabra "Python" se encuentra en el texto ingresado
if "python" in frase:
    print("La palabra python se encuentra en el texto ingresado")
else:
    print("La palabra python no se encuentra en el texto ingresado")

## con un diccionario
# options = {True: "se encuentra en el texto", False: "no se encuentra en el texto"}
# python_in_text = "python" in frase
# print(f"La palabra python {options[python_in_text]}")