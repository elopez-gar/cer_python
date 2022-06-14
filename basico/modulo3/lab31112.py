#Laboratorio 3.1.1.12
#Elaborado por: Emmanuel López García
#Fecha: 14 de junio del 2022

#FALTA TERMINAR
year = int(input("Introduce un año: "))

#
# Escribe tu código aquí.
#	

if year <= 1582:
    print("No dentro del período del calendario Gregoriano")
if not (year % 4 == 0):
    print("Año Común")
elif not (year % 100 == 0):
    print("Año Bisiesto")
elif not (year % 400 == 0):
    print("Año Común")
else:
    print("Año Bisiesto")
