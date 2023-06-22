#Ejercicio 1: Vehículo pt.1
#A partir del siguiente diagrama de clases, implementá
#clases y métodos para mostrar atributos.

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, velocidad, cilindrada, color, ruedas):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def mostrar_datos(self):
        return f"El color del vehiculo es {self.color}, tiene {self.ruedas} ruedas. La velocidad máxima es de {self.velocidad}km/h y es de {self.cilindrada}cc"


coche1 = Coche( 220, 2.0, "Negro", "5")

print(coche1.mostrar_datos())
    
        
