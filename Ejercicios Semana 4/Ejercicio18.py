lista_a_calcular = []
user_input = input("Ingrese una lista de números separados por espacios o comas: ").split()
for item in user_input:
    lista_a_calcular.append(int(item))

def  calcular_mayor_diferencia(lista):
    mayor = max(lista)
    menor = min(lista)
    diferencia_maxima = mayor - menor
    return diferencia_maxima

print(f"La mayor diferencia entre los números de la lista es: {calcular_mayor_diferencia(lista_a_calcular)}")