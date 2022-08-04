#Laboratorio 3.2.1.14
#Elaborado por: Emmanuel López García
#Fecha: 03 de agosto del 2022

# Creando superclase llamada Stack
class Stack:
    def __init__(self): # Método
        self.__stk = []

    def push(self, val): # Método
        self.__stk.append(val)

    def pop(self): # Método
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

class CountingStack(Stack): # Subclase
    def __init__(self): # Método
        Stack.__init__(self)
        self.__contador = 0

    def get_counter(self): # Método
        return self.__contador

    def pop(self): # Método
        self.__contador += 1
        return Stack.pop(self)


stk = CountingStack() # Objeto
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())