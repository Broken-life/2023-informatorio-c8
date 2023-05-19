cadena_uno = input("Ingrese la primera cadena de texto: ")
cadena_dos = input("Ingrese la segunda cadena de texto: ")

def es_anagrama(cadena1, cadena2):
    if len(cadena1) != len(cadena2):
        return False
    else:
        for letra in cadena1:
            if letra not in cadena2:
                return False
        return True

print(es_anagrama(cadena_uno, cadena_dos))