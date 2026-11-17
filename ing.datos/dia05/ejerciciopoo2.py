class Animal:
    def __init__(self, nombre):
        self.nombre=nombre
    def saltar(self):
        print(f"{self.nombre}ha saltado")
class Gato(Animal):
    def hablar(self):
        self.hablar="miau"
        print(f"el gato dice {self.hablar}")
pelusa = Gato("michi")
pelusa.saltar()
pelusa.hablar()