filas = int(input("Ingrese un numero para crear el triángulo: "))

for i in range(filas):
    for j in range(i+1):
        print(i+1, end=" ")
    print("")