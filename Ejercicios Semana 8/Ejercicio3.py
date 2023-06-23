class Triangulo:
    def __init__(self):
        self.lado1 = int(input("Ingrese el lado 1: "))
        self.lado2 = int(input("Ingrese el lado 2: "))
        self.lado3 = int(input("Ingrese el lado 3: "))

    def lado_mayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            return self.lado1
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            return self.lado2
        else:
            return self.lado3

    def tipo_triangulo(self):
        if self.lado1 == self.lado2  == self.lado3:
            return "Equilatero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isosceles"
        else:
            return "Escaleno"
    
    def imprimir(self):
        print("Lado mayor: ", self.lado_mayor())
        print("Tipo de triangulo: ", self.tipo_triangulo())

triangulo = Triangulo()
triangulo.imprimir()

