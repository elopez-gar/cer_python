#Laboratorio 2.8.1.4
#Elaborado por: Emmanuel López García
#Fecha: 31 de julio del 2022

def read_int(prompt, min, max):
    bien = False
    while not bien:
        try:
            valor = int(input(prompt))
            bien = True
        except ValueError:
            print("Error: entrada incorrecta")
        if bien:
            bien = valor >= min and valor <= max
        if not bien:
            print("Error: el valor no esta dentro del rango permitido (" + str(min) + ".." + str(max) + ")")
    return valor;


v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)