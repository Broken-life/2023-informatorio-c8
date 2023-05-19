number = int(input("Ingrese un número: "))

def es_par(number):
    if number % 2 == 0:
        return print("Es par")
    else:
        return print("Es impar")
    
es_par(number)