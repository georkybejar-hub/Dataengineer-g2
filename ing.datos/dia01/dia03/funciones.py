def saludar_persona(nombre="invitado"):
    print(f"Hola, {nombre}!")
saludar_persona()




"""funciuones con numeros variable de argumentos"""
"""args = *  """
def sumar_numeros(*numeros):
    print(numeros)

sumar_numeros(1, 2, 3, 4, 5)


def mostrar_numeros(*args):
    for numero in args:
        print(numero)

mostrar_numeros(10, 20, 30, 40, 50)



"""kwargs = **"""
def mostrar_informacion(nombre, edad):
    print(nombre, edad)

mostrar_informacion(nombre="Alice", edad=30)



"""2 ejemplo"""
def mostrar_informacion(**kwargs):
    for clave in kwargs:
        print(clave, kwargs[clave])
mostrar_informacion(nombre="Alice", edad=30, ciudad="Madrid")