"""son colecciones ordenadas y """
lista1 = ["Georky", "Juan", "Pedro", "Maria", "Jose"]
lista2 = [1, 2, 3, 4, 5]
lista3 = [True, False, True, False]
print(lista1[1])


"""slicing/(rebanado)"""
print (lista2[1:3]) 
print(lista1[::2])

"""modificar elementos de la lista"""
lista2[0] = 10
print(lista2)

"""agregar listas"""
lista2=lista2 + [6, 7, 8]
print(lista2)


""""obtener la logitud de la lista"""
print(len(lista1))

"""metodos de listas"""
lista= ["Python"]
lista.append("Java")
print(lista)

"""ES PARA INSERTAR UN VALOR PERO YO ELIGO LA POSICION"""
lista.insert(0,"C++")
print(lista)
"""ES PARA ELIMINAR UN ELEMENTO DE LA LISTA"""
lista.remove("Java")
print(lista)

""""lelimina el primer elemento de la lista"""
lista.pop(0)
print(lista)



print(lista.index("Python"))


print(lista.count("Python"))

Listaa2 = [5 ,10,12,6,1,3,20]
Listaa2.sort()
print(Listaa2)


Listaa2.reverse()
print(Listaa2)

Listaa2.clear()
print(Listaa2)
