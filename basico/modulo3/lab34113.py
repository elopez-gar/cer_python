#Laboratorio 3.4.1.13
#Elaborado por: Emmanuel López García
#Fecha: 16 de junio del 2022

# paso 1
from curses import beep


beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
print("Ingrese los siguientes nombres a la lista: Stu Sutcliffe y Pete Best")
for i in range(2):
    beatles.append(input())
print("Paso 3:", beatles)

# paso 4
for i in range(2,0,-1):
    del beatles[-i]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))
