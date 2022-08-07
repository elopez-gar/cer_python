#Laboratorio 4.3.1.15
#Elaborado por: Emmanuel López García
#Fecha: 04 de agosto del 2022

# ¡NOTA IMPORTANTE!: LEER LOS COMENTARIOS QUE VIENEN AL FINAL DEL CÓDIGO 

from os import strerror

contador = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
archivo = input("Indica el nombre del archivo: ")
try:
    file = open(archivo, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                contador[char.lower()] += 1
    file.close()
    for char in contador.keys():
        c = contador[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

# Nota 1: Hay un archivo con el nombre "prueba.txt" que sirve para verificar este laboratorio

# Nota 2: Es importante ubicarse en el DIRECTORIO en el que se encuentra la
#   ruta del laboratorio actual con la finalidad de que se cree el archivo correctamente.
