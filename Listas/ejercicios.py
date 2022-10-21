# EJERCICIOS LISTAS

#Ejercicios manipulacion

#1. Consiste en la definicion de una lista con elementos de diferentes tipos y en monstrarla por pantalla, tanto entre como elementos accedirndo a la posicion que ocupa dentro de la lista.
lista = ["Python", "Guanenta", 2022, "libro", 3]
print(lista)
print(lista[0])
print(lista[2])

# 2. Consiste en el uso del operador + para re alizar uniones de lsitas. Ademas utilizar la funcion len para conocer el numero de elementos que componen la lista
lista1 = ["Camiseta", "Pantalon", "Zapatillas"]
lista2 = ["Abrigo", "Jersey", "Sudadera", "Calceines"]
print("Numero elementos lista1: ", len(lista1))
print("lista1: ", lista1)
print("Numero elementos lista2: ", len(lista2))
print("lista1: ", lista2)
lista_concatenada = lista1 + lista2
print("Numero elementos lista_concatenada: ", len(lista_concatenada))
print("lista_concatenada: ", lista_concatenada)

# 3. Añadir elementos a la lista de diferentes formas
lista = ["Camiseta", "Pantalon", "Zapatillas"]
print(lista)
lista = lista + ["Abrigo"]
print(lista)
lista = lista + ["Jersy", "Sudadera"]
print(lista)
lista = lista + ["Calcetines"]+["Bufanda"]
print(lista)

# 4. Modificar elementos de una lista y borrar elementos de la misma
lista = ["Camiseta", "Pantalon", "Zapatillas"]
print(lista)
lista[1] = "Cazadora"
print(lista)
del lista[0]
print(lista)

# 5. Uso del operador *. Permite concatenar una lista con ella misma un numero finito de veces.
lista = ["Camiseta", "Pantalon", "Zapatillas"]
print(lista)
lista_resultante = lista * 3
print(lista_resultante)

# 6. Creacion de listas como elementos de listas y accesos a dichos elementos.
print("-----Ejercicios 6 -----")
lista = ["Camiseta", ["Calcetines", "Cazadores"], "Zapatillas"]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1][0])
print(lista[1][1])

# 7. Estraer una porcion de la lista en una lista nueva
print("-----Ejercicios 7 -----")
lista = [1,2,3,4,5,6,7,8,9]
print(lista)
lista1 = lista[3:7]
print(lista1)
lista2 = lista[:5]
print(lista2)
lista3 = lista[6:]
print(lista3)