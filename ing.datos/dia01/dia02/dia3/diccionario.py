users= [
    ["Juan", 25, "M", "juan@example.com"],
    ["María", 30, "F", "maria@example.com"],
    ["Carlos", 28, "M", "carlos@example.com"],
    ["Ana", 22, "F", "ana@example.com"],
]

user_format ={
    "id": 1,
    "nombre": "Juan",
    "edad": 25,
    "genero": "M",
    "email": "juan@example.com"
}
new_user = []
i=1
for user in users:
    user_dict = {
        "id": i,
        "nombre": user[0],
        "edad": user[1],
        "genero": user[2],
        "email": user[3]
    }
    i+= 1
    new_user.append(user_dict)

print(new_user)





vehiculos = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020,
}

"""modifica y agregar elementos al diccionario"""
vehiculos["color"] = "Rojo"
vehiculos["año"] = 2021
vehiculos["marca"] = "Honda"

print(vehiculos)


"""elminiar elementos del diccionario """
del vehiculos["modelo"]
print(vehiculos)


"""Metodos Utiles de los diccionarios"""
print(vehiculos.keys())
print(vehiculos.values())
print(vehiculos.items())


"""interar con diccionarios"""
for clave in vehiculos:
    print(clave, vehiculos[clave])