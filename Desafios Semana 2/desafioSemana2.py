### ---Desafio 2 --- ### 
frase = str(input("Ingrese una frase, palabra, o texto:").lower()) 

#reemplazamos los caracteres que no sean letras, numeros o espacios por un espacio vacio
for caracter in frase:
    if caracter.isalpha() or caracter.isdigit() or caracter.isspace():
        continue
    else:
        frase = frase.replace(caracter, '')

letras_elegidas = []
for letra in range(3):
    letras_elegidas.append(str(input(f"Ingrese una letra {letra+1}: ").lower()))

#cantidad de veces que aparece cada letra elegida en el texto ingresado
for letra in letras_elegidas:
    cant_letras = frase.count(letra) 
    print(f"La letra {letra} aparece {cant_letras} veces")

#cantidad de palabras que tiene la frase ingresada
frase.split()
longitud_frase = len(frase.split())
print(f"La frase ingresada tiene {longitud_frase} palabras")

#primera letra y ultima letra de la frase ingresada
primera_letra = frase[0]
ultima_letra = frase[-1]
print(f"La primera letra de la frase es {primera_letra} y la última letra es {ultima_letra}")

#mostrar el texto ingresado, en orden inverso
frase_invertida = frase[::-1]
print(f"El texto ingresado en orden inverso es: {frase_invertida}")

#Usando un diccionario para determinar si "python" se encuentra en el texto ingresado":
python_in_text = "python" in frase
options ={"si": True , "no": False} 
if python_in_text == options["si"]:
    print("La palabra 'Python' se encuentra en el texto ingresado :) ")
else:
    print("La palabra 'Python' no se encuentra en el texto ingresado :( ")

