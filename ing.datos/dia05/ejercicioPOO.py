"""
Recuperar la información de datos.csv y construir una lista de
diccionario con estos datos, además se debe ordenar por orden alfabético
en base a los apellidos, también se les debe generar una contraseña
encriptada por defecto en base a la fecha de nacimiento.

# Output [{"id": 1, "nombre": "...", "apellido": "...", "activo": True}, {}, ..., {}]
"""
import csv
import hashlib
class Usuario:
    def __init__(
        self,
        id,
        nombre,
        apellido,
        email,
        telefono,
        ciudad,
        pais,
        fecha_registro,
        activo
  
    ):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.ciudad = ciudad
        self.pais = pais
        self.fecha_registro = fecha_registro
        self.activo = activo
        self.password = self.__generar_password_encriptada()

    def __generar_password_encriptada(self):
        fecha_registro_bytes = self.fecha_registro.encode("utf-8")
        return hashlib.sha256(fecha_registro_bytes).hexdigest()
    
    
    
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
            "activo": self.activo,
            "password":self.password

        }

def main():
    usuario_objeto = []
    with open("datos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        n_fila = 0

        for fila in lector:
            n_fila = n_fila + 1

            if n_fila == 1:
                continue

            usuario = Usuario(*fila)
            usuario_objeto.append(usuario)

    def obtener_apellido(usuario):
        return usuario.apellido.lower()    
    usuario_ordenados = sorted(
        usuario_objeto,
         key= obtener_apellido
     )

    resultado_final=[]
    for user in usuario_ordenados:
        resultado_final.append(user.to_dict())
    print(resultado_final)
      
if __name__ == "__main__":
    main()