fechaActual = input("Ingrese la fecha actual en el formato (dd/mm/aaaa): ")
fechaNacimiento = input("Ingrese la fecha de nacimiento en el formato (dd/mm/aaaa): ")

listaA= fechaActual.split("/")
listaN= fechaNacimiento.split("/")

print("La edad de la persona es: ", int(listaA[2])-int(listaN[2]))