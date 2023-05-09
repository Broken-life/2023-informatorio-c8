number = int(input("Escribe un número: "))
suma_divisores = []

for i in range(1, number):
    if number % i == 0:
        suma_divisores.append(i)

if sum(suma_divisores) == number:
    print("El número", number, "es perfecto")
else:
    print("El número", number, "no es perfecto")