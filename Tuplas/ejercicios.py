# En el siguiente ejercicio vamos a ver como definir tupla y como acceder a sus elementos. El codigo fuente es el sigueinte:
tupla = ('Casa','2','345','Perro',99)
print("Elementos de la tupla: ", tupla)
print("Elemtos de la posicion 0: ",tupla[0])
print("Elemtos de la posicion 1: ",tupla[1])
print("Elemtos de la posicion 2: ",tupla[2])
print("Elemtos de la posicion 3: ",tupla[3])
print("Elemtos de la posicion 4: ",tupla[4])

# Funcion count: cuenta el numero de veces que aparece el elemento indicado como parametro dentro de la tupla
# Funcion index: Devuelve la posicion de la primera ocurrencia de izquierda a derecha en la lista, del elemento pasado como parametro

# A continuacion vamos a hacer realizar un ejercicio para aprender a utilizar ambas funciones de las tuplas. El codigo fuente es el siguiente:
tupla = ("Casa","2",99,345,"Perro",99)
print("Elemtos de la tupla: ",tupla)
print("Numero de elementos 99: ",tupla.count(99))
print("Posicion que ocupa el elmento Perro: ",tupla.index("Perro"))

#Las tuplas, al igual que las listas, permiten extraer pociones de ellas en otra tupla nueva. La extracion se realizar utilizado la siguiente instruccion: 
# Tupla[n:m]

# La instruccion extraera una nueva tupla que empezara en el indice n y terminara en el m-1. Tienes que tener en cuenta lo siguiente:

# n siempre tiene que ser menor que m
# Si no se especifica el valor para n se supone que es 0.
# Si ni se especifica el valor para m se supone que es el tamaño de la lista menos un

# Veamoslo en un ejercicio, el codigo
tupla = (1,2,3,4,5,6,7,8,9)
print(tupla)
print(tupla[4:9])
print(tupla[:3])
print(tupla[2:])

#La siguiente funcionalidad de las tuplas que vamos a explicar es el uso del operador "+" para realizar uniones de tuplas. El operador se utilza de la siguinte manera: 
# TuplaConcatada = Tupla+Tuplas2

#Ademas, vamos a aprender a utilizar una funcion para conocer el numero de elementos que componen la tupla. Dicha funcion se llama len y delvelve un entero que indica el numero de elementos que la componen. Se utilizade la siguiente manera: 
#NumeroElementos=len(Tupla)

# El codigo fuente del ejercicio es el siguiente:

tupla1 = (29, "Television",8763)
tupla2 = (1,2,3, "Videojuego")
print("Numero elementos de tupla1: ",len(tupla1))
print("Tupla1: ", tupla1)
print("Numero elementos de tupla2: ",len(tupla2))
print("Tupla2: ", tupla2)
tuplaconcatenada = tupla1 + tupla2
print("Numero elementos de tuplaconcatenada: ",len(tuplaconcatenada))
print("tuplaconcatenada: ", tuplaconcatenada)

# La ultma funion que vamos a aprender de las tuplas es la utilizacion del operador "*", el cual nos va apermitir conectar una tupla con ella misma un numero finito de veces. El operdor se utliza de la siguiente forma:
#TuplaResultante=Tupla*NumroEntero

# La tupla resultante de la multiplicacion sera una tabla compuesta por tantas veces la Tupls como valor tenga el numero entero.

# El codigo fuente del ejercicio es el siguiente:
tupla = (1,2,3,4,5,6,7,8,9,0)
print(tupla)
tuplaresultante = tupla * 4
print(tuplaresultante)