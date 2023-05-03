import datetime
fecha_nac = input('Ingrese su fecha de nacimiento dd/mm/aaaa: ')
dia, mes, anio = map(int, fecha_nac.split('/'))

fecha_act = datetime.date.today()
anio_hoy = fecha_act.year
mes_hoy = fecha_act.month
dia_hoy = fecha_act.day

edad = anio_hoy - anio

if(mes > mes_hoy):
    edad = edad - 1
    print('Tu edad actual es de '+str(edad)+' años')
elif((mes == mes_hoy) and (dia == dia_hoy)):
    print("¡¡¡felices", edad, "años!!!")
elif((mes == mes_hoy) and (dia < dia_hoy)):
    print("feliz cumple numero", edad, "atrasado, jeje")
elif((mes == mes_hoy) and (dia <= dia_hoy+3)):
    print("falta poco para tu cumpleaños numero", edad)
else:
    print('Tu edad actual es de '+str(edad)+' años')
