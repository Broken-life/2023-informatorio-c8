nro_entero = int(input("Ingrese un número entero: "))

def imprimir_pares(nro):
    for i in range(1, nro + 1):
        if i % 2 == 0:
            print(f"{i} es par")

imprimir_pares(nro_entero)