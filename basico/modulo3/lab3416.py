#Laboratorio 3.4.1.6
#Elaborado por: Emmanuel López García
#Fecha: 16 de junio del 2022

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
print("Lista inicial:", hat_list)
# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
num = int(input("Ingrese un número entero que reemplazará al de en medio: "))
hat_list [2] = num
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Lista final:",hat_list)
