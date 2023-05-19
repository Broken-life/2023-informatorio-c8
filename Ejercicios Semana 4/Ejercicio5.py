number1 = int(input("Ingrese el numero a dividir: "))
number2 = int(input("Ingrese el numero divisor: "))

def es_divisible(nro1, nro2):
        if nro1 % nro2 == 0:
            return print("Es divisible")
        else:
            return print ("No es divisible")

es_divisible(number1, number2)