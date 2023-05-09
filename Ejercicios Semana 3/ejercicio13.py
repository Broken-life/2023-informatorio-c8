filas = int(input("Ingrese el numero de filas que tendrá el triángulo: "))

for i in range(filas+1):
    for j in range(i):
        print("*", end="")
    print("")
