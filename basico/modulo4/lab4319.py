#Laboratorio 4.3.1.8
#Elaborado por: Emmanuel López García
#Fecha: 24 de junio del 2022

def is_prime(num):
#
# Escribe tu código aquí.
#
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor += 1
    return True


   # num = int(input("Ingresa el valor: "))

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
