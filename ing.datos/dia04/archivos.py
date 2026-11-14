archivo = open("datos.txt", "r")
contenido = archivo.read()
archivo.close()
print(contenido)

#"r" para lectura
#"encoding="utf-8":evita errores en tildes, Ñ y caracteres especiales
#with: gestiona recursos de forma segura y automtica.
#.read()= para leer el archivo

with open("datos.txt","r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)


"""leer linea por linea"""
with open("datos.txt","r", encoding="utf-8") as archivo:
    rows = 0
    for linea in archivo:
        rows += 1
        if rows ==1:
            continue
        lineas_sin_espacio = linea.strip()
        lenguaje = lineas_sin_espacio.split(",")[-1]
        print(lenguaje)



"""guardar las lineas en una lista"""
with open("datos.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()



"""formatos estrucutrados comunes(csv y json)"""
import json
with open("datos.json","r", encoding="utf-8")as archivo:
    datos = json.load(archivo)
    print(datos)

with open("datos1.json","r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    print(datos)



"""import csv"""
import csv
with open("datos.csv","r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)