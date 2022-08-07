#Laboratorio 4.5.1.22
#Elaborado por: Emmanuel López García
#Fecha: 06 de agosto del 2022

from datetime import datetime

mi_fecha = datetime(2020, 11, 4, 14, 53)

print(mi_fecha.strftime("%Y/%m/%d %H:%M:%S"))
print(mi_fecha.strftime("%y/%B/%d %H:%M:%S %p"))
print(mi_fecha.strftime("%a, %Y %b %d"))
print(mi_fecha.strftime("%A, %Y %B %d"))
print(mi_fecha.strftime("Día de la semana: %w"))
print(mi_fecha.strftime("Día del año: %j"))
print(mi_fecha.strftime("Número de semana en el año: %W"))
