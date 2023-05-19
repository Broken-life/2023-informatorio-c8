list_number = []
numbers = input("Ingrese los números separados por coma: ").split(",")
for number in numbers:
    list_number.append(int(number))

def calcular_maximo(list_number):
    maximo = max(list_number)
    return maximo

print(f"El número máximo es: {calcular_maximo(list_number)}")