class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, velocidad, cilindrada, color, ruedas):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
class Camioneta(Coche):
    def __init__(self, velocidad, cilindrada, carga,color, ruedas):
        super().__init__(velocidad, cilindrada, color, ruedas)
        self.carga = carga

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

coche1 = Coche(150, 1200, "rojo", 4)
coche2 = Coche(200, 1600, "azul", 4)
camioneta1 = Camioneta(100, 2000, 1500, "blanco", 4)
bicicleta1 = Bicicleta("verde", 2, "urbana")
bicicleta2 = Bicicleta("negra", 2, "montaña")
motocicleta1 = Motocicleta("negra", 2, "urbana", 200, 200)
motocicleta2 = Motocicleta("roja", 2, "deportiva", 250, 250)

vehiculos = [coche1, coche2, camioneta1, bicicleta1, bicicleta2, motocicleta1, motocicleta2]

def catalogar(lista_vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [vehiculo for vehiculo in lista_vehiculos if vehiculo.ruedas == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        print()
        lista_vehiculos = vehiculos_filtrados

    for vehiculo in lista_vehiculos:
        print("Clase:", vehiculo.__class__.__name__)
        print("Atributos:")
        for atributo, valor in vars(vehiculo).items():
            print(f"{atributo}: {valor}")
        print()


catalogar(vehiculos, 0)
catalogar(vehiculos, 2)
catalogar(vehiculos, 4)


