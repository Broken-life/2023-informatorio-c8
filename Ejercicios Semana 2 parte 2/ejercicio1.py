frutas = {"manzana": 440, "pera": 500, "naranja": 350}

for fruta, precio in frutas.items():
    print(f"El precio de la {fruta} es ${precio}")

#El metodo items() devuelve una lista de tuplas, donde cada tupla es un par clave-valor