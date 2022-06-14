#Laboratorio 3.1.1.11
#Elaborado por: Emmanuel López García
#Fecha: 14 de junio del 2022

#queda pendiente
ingresos = float(input("Introduce el ingreso anual: "))

#
# Escribe tu código aquí.
#
if ingresos <= 85528:
    impuestos = ingresos*0.18 - 556.02
else:
    impuestos = 14839.02 + (ingresos-85528)*.32

impuestos = round(impuestos, 0)
print("El impuesto es:", impuestos, "pesos")

