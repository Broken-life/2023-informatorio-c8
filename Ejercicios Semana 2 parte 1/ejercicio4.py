nota = int(input("Ingrese su nota del exámen: "))

if nota >= 5 and nota <= 10:
    print("Usted está aprobado, ¡Felicidades!")
elif nota >= 0 and nota < 5:
    print("Usted está desaprobado, ¡Lo siento!")
else:
    print("La nota ingresada no es válida, por favor, ingrese una nota entre 0 y 10")
