contraseña= input("Ingrese su contraseña: ")
while len(contraseña) < 8:
    print("La contraseña debe tener al menos 8 caracteres.")
    contraseña = input("Ingrese su contraseña: ")
print("Contraseña aceptada.")


numero= int(input("Ingrese un número positivo: "))
contador=1
while contador<=10:
    resultado=numero*contador
    print(f"{numero} x {contador} = {resultado}")
    contador+=1


"""correcion contraseña"""
while True:
    password = input("Ingrese su contraseña: ")
    if len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
    else:
        print("Contraseña aceptada.")
        break
password = input("Ingrese su contraseña: ")






"""correcion segundo ejemplo"""
while True:
    number = int(input("Ingrese un número positivo: "))
    i = 1
    while i <= 10:
        result = number * i
        print(f"{number} x {i} = {result}")
        i += 1
