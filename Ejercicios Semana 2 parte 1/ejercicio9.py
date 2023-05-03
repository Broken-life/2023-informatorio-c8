num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: "))
num_3 = int(input("Ingrese otro numero: "))

if (num_1 > num_2) and (num_1 > num_3):
    print(f"El numero {num_1} es el mayor")
elif (num_2 > num_1) and (num_2 > num_3):
    print(f"El numero {num_2} es el mayor")
elif (num_3 > num_1) and (num_3 > num_2):
    print(f"El numero {num_3} es el mayor") 
else: 
    print("Los numeros son iguales")