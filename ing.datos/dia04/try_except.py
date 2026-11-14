#resutlado= 5/0
#el blqoue try se ejecuta el codigo en el que puede ocurrir un error

try:
    numero = int(input("ingresa un numero:"))
    resultado =10/numero
    print(f"el resultado es {resultado}")

#dentro de este bloque solo se ejecuta cuando ocurre un error

except ZeroDivisionError:
    print("Error:No puedes dividir entre cero.")
except ValueError:
    print("Error Debes ingresar un numero valido, no texto")
except Exception:
    print("Error: ha ocurrido un error desconocido")


#se Ejecuta solo si no hubo ningun error en el bloque try
else:
    print("Proceso finalizado cone exito")
    print(resultado)
#se ejecuta siempre (haya ocurriendo un error o no)
finally: 
    print("Proceso Finalizado")



try:
        with open("file.txt","r", encoding="utf-8") as archivo:
            contenido = archivo.read()
except FileNotFoundError:
        print("El archivo no esxite")

