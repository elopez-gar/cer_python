#Laboratorio 3.2.1.11
#Elaborado por: Emmanuel López García
#Fecha: 15 de junio del 2022
user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()
word_without_vowels = ""
vocales = "AEIOU"

for letter in user_word:  # Para cada letra que se encuentre en la variable user_word
    if letter not in vocales:  # Si la letra no está en la cadena que se especificó en vocales
        word_without_vowels = word_without_vowels + letter # Se asigna esa letra a la variable
    else:
        continue  # Se salta esa palabra ya que SI se estaría tratando de una vocal
print(word_without_vowels) # Imprime la palabra que no tiene vocales
