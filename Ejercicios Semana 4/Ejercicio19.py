year = int(input("Ingrese un año a calcular: "))

def es_bisiesto(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

print(es_bisiesto(year))