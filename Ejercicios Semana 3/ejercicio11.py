factorial = 1
number = int(input("Ingrese un numero: "))

while number != 0:
    factorial = factorial * number
    number = number -1
print(f"El factorial de su numero es: {factorial}")