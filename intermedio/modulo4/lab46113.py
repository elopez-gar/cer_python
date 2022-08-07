#Laboratorio 4.6.1.13
#Elaborado por: Emmanuel López García
#Fecha: 06 de agosto del 2022

import calendar

class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        mes_actual = 1
        numero_de_dias = 0
        while (mes_actual <= 12):
            for data in self.monthdays2calendar(year, mes_actual):
                if data[weekday][0] != 0:
                    numero_de_dias = numero_de_dias + 1

            mes_actual = mes_actual + 1
        return numero_de_dias

mi_calendario = MyCalendar()
numero_de_dias = mi_calendario.count_weekday_in_year(2000, 6)
print(numero_de_dias)
