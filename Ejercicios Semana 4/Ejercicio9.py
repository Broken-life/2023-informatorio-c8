nros = input("Ingrese una lista de números separados por coma: ").split(",")
nros = [int(i) for i in nros]

def promedio(*lista):
    suma = 0
    for i in lista:
        suma += i
    return suma/len(lista)

print(promedio(*nros))
