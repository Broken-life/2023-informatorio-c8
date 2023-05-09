num = int(input("Ingrese un numero: "))

tabla_multiplicar = 0

for i in range(0, 11):
    tabla_multiplicar = num * i
    print(f"{num} x {i} = {tabla_multiplicar}")
