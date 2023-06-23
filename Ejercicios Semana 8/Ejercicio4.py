class Tiempo:
    def __init__(self, hora = 0, minuto = 0, segundo = 0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo
    
    def __str__(self):
        return f"{self.__hora}:{self.__minuto}:{self.__segundo}"
    
    def set_hora(self, hora):
        self.__hora = hora
    
    def set_minuto(self, minuto):
        self.__minuto = minuto
    
    def set_segundo(self, segundo):
        self.__segundo = segundo

    def get_hora(self):
        return self.__hora
    
    def get_minuto(self):
        return self.__minuto
    
    def get_segundo(self):
        return self.__segundo
    
    def imprimir(self):
        print(self.__str__())

tiempo = Tiempo(12, 30, 45)

tiempo.imprimir()
tiempo.set_hora(15)
tiempo.imprimir()
tiempo.set_minuto(45)
tiempo.imprimir()
tiempo.set_segundo(30)
tiempo.imprimir()


