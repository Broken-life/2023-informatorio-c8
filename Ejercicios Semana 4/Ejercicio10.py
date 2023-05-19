number = int(input("Ingrese un número: "))
def calcular_factorial(number):
    if number == 0:
        return 1
    else:
        return number * calcular_factorial(number - 1)
factorial = calcular_factorial(number)
print(f"El factorial de {number} es {factorial}")