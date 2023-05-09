num = int(input("Ingrese un numero: "))
suma_num_naturales = 0

for i in range(1, num + 1):
    suma_num_naturales += i

print(f"La suma de los numeros naturales hasta {num} es: {suma_num_naturales}")