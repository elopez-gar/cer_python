#Laboratorio 2.6.1.11
#Elaborado por: Emmanuel López García
#Fecha: 13 de junio del 2022

hora1 = int(input("\nHora de inicio (horas): "))
minutos1 = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.

# Calculando los minutos
minutos2=((minutos1+duracion) % 60)

# calculando los minutos totales y luego lo convierte a horas
hora2= ((hora1*60 + minutos1 + duracion)//60) % 24

print("\nEl evento comienza a las: " +str(hora1) +":" +str(minutos1))
print("El evento finaliza a las: " +str(hora2) +":" +str(minutos2), "\n")
