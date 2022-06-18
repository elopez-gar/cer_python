#Laboratorio 4.3.1.6
#Elaborado por: Emmanuel López García
#Fecha: 17 de junio del 2022

def is_year_leap(year):
    if year % 4 == 0:
        return True
    elif year % 100 != 0:
        return False
    elif year % 400 == 0:
        return True
    else:
        False
#
# Escribe tu código aquí.
#

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
