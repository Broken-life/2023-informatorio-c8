from datetime import date
lista_total_inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
                        {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
                        {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
                        {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
                        {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

## interaccion con el empleado
empleado = input("Ingrese su nombre: ").capitalize()
print(f"Bienvenido {empleado} al sistema de gestión de inmuebles, ¿qué desea hacer?""\n1. Agregar un inmueble""\n2. Editar un inmueble""\n3. Eliminar un inmueble""\n4. Cambiar estado de un inmueble""\n5. Buscar inmuebles, segun presupuesto")
opcion = int(input("Ingrese el número de la opción que desea realizar: "))
while opcion < 1 or opcion > 5:
    print("La opción ingresada no es válida")
    opcion = int(input("Ingrese el número de la opción que desea realizar: "))

## reglas de validacion inmueble
def validar_inmueble(inmueble):
    if inmueble['año'] < 2000:
        return False
    if inmueble['metros'] < 60:
        return False
    if inmueble['habitaciones'] < 2:
        return False
    if inmueble['zona'] != 'A' and inmueble['zona'] != 'B' and inmueble['zona'] != 'C':
        return False
    if inmueble['estado'] != 'Disponible' and inmueble['estado'] != 'Reservado' and inmueble['estado'] != 'Vendido':
        return False
    return True

#Inmuebles totales (funcion)
def inmuebles_totales():
    print("Los inmuebles en la base de datos son:")
    for inmueble in lista_total_inmuebles:
        print(inmueble)

## Agregar un inmueble
if opcion == 1:
    inmueble = {'año': int(input("Ingrese el año de construcción: ")),
                'metros': int(input("Ingrese los metros cuadrados: ")),
                'habitaciones': int(input("Ingrese la cantidad de habitaciones: ")),
                'garaje': bool(input("Ingrese si tiene garaje (True/False): ")),
                'zona': input("Ingrese la zona (A/B/C): ").capitalize(),
                'estado': input("Ingrese el estado (Disponible/Reservado/Vendido): ").capitalize()}
    if validar_inmueble(inmueble):
        lista_total_inmuebles.append(inmueble)
        print("El inmueble se agregó correctamente")
    else:
        print("El inmueble no cumple con las reglas de validación")

## Editar un inmueble
elif opcion == 2:
    inmuebles_totales()
    inmueble = int(input("Ingrese el número del inmueble que desea editar, teniendo en cuenta que arranca desde el valor 0: "))
    if inmueble in range(0, len(lista_total_inmuebles)):
        valor_a_modificar = input(f"¿Qué desea modificar del inmueble {inmueble}? (año/metros/habitaciones/garaje/zona/estado): ").lower()
        if valor_a_modificar == 'año' or valor_a_modificar == 'metros' or valor_a_modificar == 'habitaciones':
            nuevo_valor_numerico = int(input(f"Ingrese el nuevo valor de {valor_a_modificar}: "))
            if validar_inmueble(nuevo_valor_numerico):
                lista_total_inmuebles[inmueble][valor_a_modificar] = nuevo_valor_numerico
            else:
                print("El inmueble no cumple con las reglas de validación")
        else:
            nuevo_valor_alfabetico = input(f"Ingrese el nuevo valor de {valor_a_modificar}: ").capitalize()
            if validar_inmueble(nuevo_valor_alfabetico):
                lista_total_inmuebles[inmueble][valor_a_modificar] = nuevo_valor_alfabetico
            else:
                print("El inmueble no cumple con las reglas de validación")
    else:
        print("El inmueble no existe")
        
## Eliminar un inmueble
elif opcion == 3:
    inmuebles_totales()
    inmueble = int(input("Ingrese el número del inmueble que desea eliminar, teniendo en cuenta que arranca desde el valor 0: "))
    if inmueble in range(0, len(lista_total_inmuebles)):
        lista_total_inmuebles.pop(inmueble)
        print(f"El inmueble se eliminó correctamente, la base de datos de los inmuebles quedo actualizada: {lista_total_inmuebles}")
    else:
        print("El inmueble no existe")

## Cambiar el estado de un inmueble
elif opcion == 4:
    inmuebles_totales()
    inmueble = int(input("Ingrese el número del inmueble que desea cambiar de estado, teniendo en cuenta que arranca desde el valor 0: "))
    if inmueble in range(0, len(lista_total_inmuebles)):
        estado = input("Ingrese el nuevo estado (Disponible/Reservado/Vendido): ").capitalize()
        if estado != 'Disponible' and estado != 'Reservado' and estado != 'Vendido':
            print("El estado ingresado no es válido")
        else:
            lista_total_inmuebles[inmueble]['estado'] = estado
            print(f"El estado del inmueble se cambió correctamente, la base de datos de los inmuebles quedo actualizada: {lista_total_inmuebles}")
    else:
        print("El inmueble no existe")
   
##Busqueda de inmuebles segun presupuesto
elif opcion == 5:
    presupuesto_disponible = float(input(f"{empleado}, ingrese el presupuesto disponible que posee el cliente: "))

    def precios_inmuebles(lista_total_inmuebles, presupuesto_disponible):
        year = date.today().year
        inmuebles_disponibles_cliente = []
        for inmueble in lista_total_inmuebles:
            if inmueble['estado'] == 'Disponible' or inmueble['estado'] == 'Reservado':
                if inmueble['zona'] == 'A':
                    precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500) * (1-(year - inmueble['año'])/100)
                elif inmueble['zona'] == 'B':
                    precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500) * (1-(year - inmueble['año'])/100) * 1.5
                elif inmueble['zona'] == 'C':
                    precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500) * (1-(year - inmueble['año'])/100) * 2
                if precio <= presupuesto_disponible:
                    inmuebles_disponibles_cliente.append((inmueble, precio))
        return inmuebles_disponibles_cliente
    inmuebles_disponibles_cliente = precios_inmuebles(lista_total_inmuebles, presupuesto_disponible)
    if len(inmuebles_disponibles_cliente) == 0:
        print("No hay inmuebles disponibles para el presupuesto ingresado")
    else:
        print("Los inmuebles disponibles para el presupuesto ingresado son: ")
        for inmueble in inmuebles_disponibles_cliente:
            print(f"{inmueble} Con un valor de ${inmueble[1]}")

print(f"Gracias por utilizar el sistema {empleado}, hasta pronto! :)")
