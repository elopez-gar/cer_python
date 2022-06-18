#Laboratorio 3.2.1.14
#Elaborado por: Emmanuel López García
#Fecha: 15 de junio del 2022

blocks = int(input("Ingresa el número de bloques: "))
height = 0
capa = 1
#
# Escribe tu código aquí.
#	
while capa <= blocks:
    height += 1
    blocks -= capa
    capa += 1

print("La altura de la pirámide:", height)