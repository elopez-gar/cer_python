#Laboratorio 4.3.1.16
#Elaborado por: Emmanuel López García
#Fecha: 05 de agosto del 2022

# ¡NOTA IMPORTANTE!: LEER EL COMENTARIO QUE VIENE AL FINAL DEL CÓDIGO

from os import strerror

contador = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
archivo = input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open(archivo, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                contador[char.lower()] += 1
    file.close()
    file = open(archivo + '.hist', 'wt')
    for char in sorted(contador.keys(), key=lambda x: contador[x], reverse=True):
        c = contador[char]
        if c > 0:
            file.write(char + ' -> ' + str(c) + '\n')
    file.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))


# Nota: Ahora el nombre del archivo es "prueba2.txt"