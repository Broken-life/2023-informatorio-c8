number = input("Ingrese un número: ")

def es_capicua(numero):
    if numero == numero[::-1]:
        return True
    else:
        return False
    
print(es_capicua(number))