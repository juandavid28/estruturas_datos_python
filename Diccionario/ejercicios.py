# MANIPULAION
# El primer ejercicio qe vamos a realizar referente a diccionarios seara crear uno y mostrat algunos elementos del mismo. Para acceder a los elemento del diccioanrio deberas de utilizar la clave del elemento. El codigo fuente es el siguiente:
diassemanaingles = {"Lunes" : "Monday", 
                     "Martes" : "Tuesday", 
                     "Miercoles" : "Wednesday", 
                     "Jueves" : "Thursday", 
                     "Viernes" : "Friday"}
print(diassemanaingles["Lunes"])
print(diassemanaingles["Miercoles"])
print(diassemanaingles["Viernes"])

# El siguiente ejercicio consiste en añadir elementos al diccionario, eleminar elementos del diccionario y en modificar el valor de los elementos del diccionario.
# La forma de añadir un elementos al diccionario es la siguiente:
# Diccionario[NuevaClave]=Nuevovalor
# La forma de modificar el valor de un elemento del diccionarios es la siguiente:
# Diccionario[ClaveQueseVaAModificar]=NuevoValor
# La forma de eleminiar un elemento del diccionario es la siguiente:
# del Diccionario[ClaveElementoABorrar]

# En el ejercico utilizemos el diccionario del ejercicio anterior añadiendo los dias sabado y domingo, modificando el valor de algun elementi y borrando algin elemento. El codigo fuente es el siguiente:
diassemanaingles = {"Lunes" : "Monday", 
                     "Martes" : "Tuesday", 
                     "Miercoles" : "Wednesday", 
                     "Jueves" : "Thursday", 
                     "Viernes" : "Friday"}
print(diassemanaingles)
diassemanaingles["Sabado"] = "Saturday"
print(diassemanaingles)
diassemanaingles["Domingo"] = "Sunday"
print(diassemanaingles)
diassemanaingles["Lunes"] = "MondayBORRAR"
print(diassemanaingles)
del diassemanaingles["Lunes"]
print(diassemanaingles)

# Es posible utilizar las funciones len, max y min con los diccionarios. La primera devolvera el numero de elemento que contiene el diccionario; la segunda, el elemento con el valor mayor y la tercera, el elemento con el valor menor. El valor mayor y el valor menor seran devueltos siempre que pueda calcularse dependiendo de los elementos que componen el diccionario. Veamoslo en un ejercicio. El codigo es el siguiente:
diassemanaingles = {"Lunes" : "Monday", 
                     "Martes" : "Tuesday", 
                     "Miercoles" : "Wednesday", 
                     "Jueves" : "Thursday", 
                     "Viernes" : "Friday"}
print("Numero de elmentos del diccionario: ",len(diassemanaingles))
print("Elemento mayor del diccionario:" ,max(diassemanaingles))
print("Elemento menor del diccionario: ",min(diassemanaingles))

#a continuacion vamos a realizar un ejercicio para aprender a utilizar ambas funciones de los deccionarios. El codigo fuente es el siguiente:
diassemanaingles= {"lunes":"monday","martes":"tuesday","miercoles":"wednesday","jueves":"thursday","viernes":"friday"}
print(diassemanaingles["lunes"])
print("diccionario original: ",diassemanaingles)
diccionariocopia= diassemanaingles.copy()
print("diccionario copy: ",diccionariocopia)
print("valor del lones (pop): ",diassemanaingles.pop("lunes"))
print("diccionario despues del pop: ",diassemanaingles)
print("elemento al azar con popitem: ",diassemanaingles.popitem())
print("diccionario despues del popitem: ",diassemanaingles)
print("valor del mates (get): ",diassemanaingles.get("martes"))
print("valor del lunes (get)(no existe): ",diassemanaingles.get("lunes"))
print("valor del lunes (get)(no existe): ",diassemanaingles.get("lunes","no existe"))
diassemanaingles.update({"lunes":"mondayNUEVO","martes":"tuesdayNUEVO"})
print("diccionario depues del update: ",diassemanaingles)
print("setdefault del sabado: ",diassemanaingles.setdefault("sabado","saturday"))
print("diccionario despues del setdefault (nuevo elemento): ",diassemanaingles)
print("setdefault del lunes: ",diassemanaingles.setdefault("lunes","lunes"))
print("diccionario despues del setdefault (elemento existente): ",diassemanaingles)
print("elemento iterable (items): ",diassemanaingles.items())
print("elemento iterable (claves): ",diassemanaingles.keys())
print("elemento iterable (valores): ",diassemanaingles.clear())
print("diccionario despues del clear: ",diassemanaingles.clear())
