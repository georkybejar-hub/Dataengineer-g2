lista = ["python", "java", "c++", "c#", "php", "javascript"]

"""Recorrer una lista"""
for lenguaje in lista:
    print(lenguaje)

"""Recorrer cadena de texto"""
texto = "Hola mundo"
for letra in texto:
    print(letra)


"""Recorrer una lista con range"""
for index, lenguaje in enumerate(lista):
    print(index, lenguaje)
