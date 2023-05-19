precio = float(input("Ingrese el precio del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

def calcular_descuento(precio, porcentaje_descuento):
    descuento = precio * (porcentaje_descuento / 100)
    precio_final = precio - descuento
    return precio_final

print(f"El precio final, aplicando el descuento es: ${calcular_descuento(precio, porcentaje_descuento)}")
