nros_pares = []
suma_pares = 0

for i in range(1, 101):
    if i % 2 ==0:
        nros_pares.append(i)
        for i in nros_pares:
            suma_pares += i
print(f"La suma de los numeros pares entre 1 y 100 es: {suma_pares}")