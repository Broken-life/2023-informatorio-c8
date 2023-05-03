number1 = int(input("Ingrese un número entero: "))
number2 = int(input("Ingrese otro número entero: "))

if number1 > number2:
    print(f"El número {number1} es mayor que el número {number2}")
elif number2 > number1:
    print(f"El número {number2} es mayor que el número {number1}")
else:
    print(f"Los números ingresados, {number1} y {number2} son iguales")