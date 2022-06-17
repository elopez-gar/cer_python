#Laboratorio 3.6.1.9
#Elaborado por: Emmanuel López García
#Fecha: 17 de junio del 2022

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista = []

# Escribe tu código aquí.
#
for i in my_list:
    if i not in lista:
        lista.append(i)
lista.sort()
print("La lista con elementos únicos:")
print(lista)
