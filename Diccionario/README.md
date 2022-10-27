# DICCIONARIOS

- En este apartado vamos a hablar sobre los tipos de datos diccionarios, que son un conjunto ordenado de elementos cuyos indices no son numeriocos sino identificadores. Al igual que las listas y las tuplas, los diccionarios puede contener datos de cualquier tipo. En otras palabras, los diccionarios son colecciones de elementos compuestos por una clave y un valor asociado, con la caracteristica de que las claves no pueden repetirse.

- Los diccionarios en Python se delimitan por corchetes "{}", con los elementos separados por comas y clave separada del valor mediante don puntos. Veamos un ejemplo de diccionario:
{"Clave1":"Valor1","Clace2":"Valor2","Clave3":"Valor3"}

- El diccionario de ejemplos esta compuesto por tres elementos, en la siguiente tabla te mostramos la relacion entre clave y el valor asociado:

|Clave|Valor|
|------|--------|
|"Clave1"|"Valor1"|
|"Clave2"|"Valor2"|
|"Clave3"|"Valor3"|

- Aunque puedes utilizar todos ellos como clave, los mas comunes son cadenas de texto y enteros.

# Ejecicios
Los ejericicios con diccionarios los hemos dividido en dos grupos diferentes. El primer grupo de ejercicios consiste en el aprendizaje de los metodos propios de los diccionarios y el segi¿undo grupo consiste en el aprendizaje de los metodos propios de los tiempos de datos diccionario.

# METODOS PROPIOS
- El tipo de dato diccionario en python posee una serie de funciones que nos permite manipular los diccionarios realizando operaciones complejas de forma sencilla y con una simple instruccion. El formato de uso de la gran mayoria de las funciones es el siguiente:
Diccionario.NombreFuncion(Parametros)

- Veamos en detalle cada una de las partes

1. Diccionario:Diccionario que ejecuta la funcion.
2. NombreFuncion:nombre de la funcion que se requiere ejecutar
3. Parametro: no todas las funciones tiene parametro para ejecutarse, esta parte ed dependiente de la funcion que se quiere ejecutar

- La funcion de lista que pone a nuestra disposicion Python son las siguientes:

1. copy:realiza una copia exacta del diccionario en uno nuevo.
    1. Valor devuelto:diccionario copiado.
    2. Parametros:no tiene.

2. pop: obtiene el valor de la clave pasada como parametro y ademas elimina el elmento del diccionario.

    1. Valor devuelto:valor del elemento o error en caso de no encontrar la clave del diccionario
    2. Parametros: clave a buscar en el diccioanrio

3. popitem: obtiene un elemento aleatorio del diccionario y elimina del mismo.
    1. Valor devuelto: elemento del diccionario y en caso de que no tenga elementos el diccionario da un error.
    2. Parametros: no tiene.

4. get:obtiene el valor de la clave pasada como parametro.
    1. Valor devuelto:devolvera el valor dle elemento en caso de existir dicha clave y en caso de no existir devolvera "None". Existe la posibilidad de especificar mediante un segundo paramentro un valor diferente a "None" como retorno en casi de no existir la clave.
    2. Parametro: Tiene dos parametros, el primero es obligatorio y es clave del elemento a buscar y el segundo es opcional y es el valor que quiere retornar en caso de no existir dicha clave en el diccionario

5. update: realizar una actualizacion del diccioanrio utilizado otro diccioanrio aquellos elementos del diccioanrio que se utilizan para actualizar el principal sustituiran los existentes en el mismo y aquellos elementos que no exitan seran añadidos al diccionairio como nuevos elementos
    1. Valor devuelto:nuevo diccioanrio
    2. Parametro:diccioanrio

6. setdefault: intenta insetar un elemento (clave y valor) en el diccionario. En caso de noexistir dicho elemento y en caso de existi, lo unico que haces es devolver el valor actual.
    1. Valor devuelto: diccionario resultante.
    2. Parametros: dos parametros que son la clave y el valor. Es posible no especificar el valor y por defecto se insertara el valor None como valor del elemento

7. clear: elimina todos los elementos del diccionario
    1. Valor devuelto:diccioanrio vavio.
    2. Parametro:no tiene

8. items: devuleve un objeto iterable compuestos por todos los elemetos del diccioanrio
    1. Valor devuelto: objeto iterable compuesto por los elementos del diccioanrio
    2. Parametros: no tiene.

9. keys: devuelve un objeto iterable compuesto por todas las claves del diccioanrio
    1. Valor devuelto: objeto iterable compuesto por las claves del diccionario
    2. Parametros: no tiene.

10. values: devuelve un objeto iterable compuesto por todos lso valores del diccioanrio
    1. Valor devuelto: objeto iterable compuesto por los valores del diccionario.
    2. Parametos: no tiene