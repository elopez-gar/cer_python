#Laboratorio 3.2.1.15
#Elaborado por: Emmanuel López García
#Fecha: 15 de junio del 2022

c0 = int(input("Ingrese un numero: "))

pasos = 0
 
while c0 > 1: # Mientras el número ingresado por el usuario sea mayor a 0
    if c0 %2 == 0: # Si el número ingresado es número par
        c0 = c0 // 2 # Se divide el número ingresado entre dos
        pasos += 1  # Aumenta la cantidad de pasos a la variable pasos
        print(c0)
    elif c0 != 0:
        c0 = 3 * c0 + 1
        pasos += 1
        print(c0)
 
print("Pasos: ",pasos) # En cada vuelta al ciclo se está incrementando la variable pasos