class Persona:
    print
class Vehiculo:
    def __init__(self, marca ,color ,modelo):
        self.marca = marca
        self.modelo= modelo
        self.color=color
        self.__codigo= "wdwddw"
    def ver_datos(self):
        print(f"Este vehiculo es de marca; {self.marca}, color:{self.color}, modelo{self.modelo}, y codido{self.__codigo}")
    def __informacion_privada(self):
        print(f"Esta informacion es privada:{ self.__codigo}")
camioneta = Vehiculo("Toyota","Hilux", "Blanco")
print(camioneta)

coche = Vehiculo("vm", "golf", " negro")
print(coche.color)
coche.ver_datos()
print(coche.__codigo)
coche.__informacion_privada()


        
