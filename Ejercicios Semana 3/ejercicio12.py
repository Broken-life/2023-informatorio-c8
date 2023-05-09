numbers = input("Ingrese una lista de numeros separados por coma: ")
numbers = numbers.split(",") 
suma = 0
for i in range(len(numbers)):
    suma = suma + int(numbers[i])
    promedio = suma / len(numbers)
print("El promedio de los numeros ingresados es: ", promedio)