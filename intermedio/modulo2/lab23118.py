#Laboratorio 2.3.1.18
#Elaborado por: Emmanuel López García
#Fecha: 29 de julio del 2022

def mysplit(strng):
    #
    # coloca tu código aquí
    #
    if strng == '' or strng.isspace():
        return []
    
    lista = []
    palabra = ''
    enpalabra = not strng[0].isspace()

    for x in strng:
        if enpalabra:
            if not x.isspace():
                palabra = palabra + x
            else:
                lista.append(palabra)
                enpalabra = False
        else:
            if not x.isspace():
                enpalabra = True
                palabra = x
            else:
                pass
    if enpalabra:
        lista.append(palabra)
    return lista
        

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
