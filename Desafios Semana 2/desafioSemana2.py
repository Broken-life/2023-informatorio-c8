frase = str(input("Ingrese una frase, palabra, o texto:").lower()) #pasamos todo a minuscula

#metemos las letras en una lista
letras = []

letras.append(input("Ingrese la una letra: "))
letras.append(input("Ingrese la otra letra: "))
letras.append(input("ingrese la ultima letra: "))

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
