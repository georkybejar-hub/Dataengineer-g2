"""
Recuperar la información de datos.csv y construir una lista de
diccionario con estos datos, además se debe ordenar por orden alfabético
en base a los apellidos, también se les debe generar una contraseña
encriptada por defecto en base a la fecha de nacimiento.

# Output [{"id": 1, "nombre": "...", "apellido": "...", "activo": True}, {}, ..., {}]
"""

class Usuario:
    def __init__(self):
        self.id = 1
        self.nombre = "Lucía"
        self.apellido = "Mendoza"
        self.email = "email@email.com"
        self.telefono = "987654321"
        self.ciudad = "Arequipa"
        self.pais = "Perú"
        self.fecha_registro = "2025-01-01"
        self.activo = True
    #construir el diccionario
    def to_dict(self):
        return {
            "id":self.nombre,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "telefono":self.telefono,
            "ciudad":self.ciudad,
            "pais":self.pais,
            "fecha_registro":self.fecha_registro,
            "activo": self.activo

        }
usuario = Usuario()
usuario_dict= usuario.to_dict()
print(usuario_dict)