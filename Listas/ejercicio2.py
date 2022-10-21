# EJERCICIOS LISTAS

#Metodos propios

lista = [45, 32, 3, 78]
print("lista original: ", lista)
# Funcion append: añande un elemento a la lista
lista.append(995)
lista.append(7)
print("Lidta despues de usar append: ", lista)
# Funcion sort: ordena la lista
lista.sort()
print("Lista ordenada:", lista)
# Funcion reverse: Invierte el orden de la lista
lista.reverse()
print("Lista al reves: ", lista)
# Funcion extend: añade los elmentos de una lista a la lista
lista_extend = [1,5,87,45]
lista.extend(lista_extend)
print("Lista de extend", lista)
# FUncion count: cuenta el numero de veces que aparece el elemento indicado como parametro dentro de la lista
print("Numero de elementos 45: ", lista.count(45))
# Funcion inset: añade el elemento pasado como parametro a la lista en la posicion indicada tambien por parametro
lista.insert(4,111)
print("Lista despues de insert: ", lista)
# Funcion remove: elimina la primera ocurrencia empezada por la izquierda de la lista del elemento indicado como parametro
lista.remove(45)
print("LIsta despues de rmove:", lista)
# Funcion index: Devuelve la posicion de la primera ocurrencia de izquierda a derecha en la lista, del elemento pasado como parametro
print("Posicion del elemeto 111: ", lista.index(111))
# Funcion pop: Elimina el ultimo elemento de la lista y lo delvuelve como resultado de la operacion
lista.pop()
print("Lista despues de pop: ", lista)
# Funcion clear: Elimina tosdos los elementos de la lista
lista.clear()
print("Lisa despues de clear: ", lista)