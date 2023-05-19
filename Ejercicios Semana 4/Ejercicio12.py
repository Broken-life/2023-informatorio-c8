temp = float(input("ingrese una temperatura: "))

def convertir_temperatura(temp):
    Fahrenheit = (temp * 9/5) + 32
    return Fahrenheit

print(f"La temperatura en Fahrenheit es: {convertir_temperatura(temp)}")