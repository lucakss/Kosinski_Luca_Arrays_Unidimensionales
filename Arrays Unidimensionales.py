#1 Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
def crear_array(cantidad: int) -> list:
    array = [0] * cantidad
    
    return array

array = crear_array(5)

#2 Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.
def ingresar_elementos(array: list, cantidad: int) -> list:
    
    for i in range(cantidad):
        numero = int(input(f"Ingrese un numero para la posicion {i}: "))
        array[i] = numero
    #No hace falta el return pq el array va mutando

ingresar_elementos(array, 3)
print(array)

#3 Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 
def calcular_promedio(array: list) -> float:
    largo = len(array)
    suma = 0
    
    for i in range(largo):
        suma += array[i]
        
    promedio = suma / largo
    return promedio

array = [7, 7, 6]
promedio = calcular_promedio(array)
print(promedio)

#4 Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
def calcular_promedio_positivos(array: list) -> float:
    contador = 0
    suma = 0
    
    for i in range(len(array)):
        if array[i] > 0:
            contador += 1
            suma += array[i]
                    
    promedio = suma / contador
    return promedio

array = [7, 7, 6, -1, -2, -3]
promedio = calcular_promedio_positivos(array)
print(promedio)

#5 Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
def calcular_producto(array: list) -> float:
    producto = 1
    
    for i in range(len(array)):
        producto *= array[i]
        
    return producto

array = [7, 7, 6]
producto = calcular_producto(array)
print(producto)

#6 Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
def calcular_maximo(array: list) -> int:
    incide_maximo = 0
    maximo = array[0]
    
    for i in range(len(array)):
        if array[i] > maximo:
            maximo = array[i]
            incide_maximo = i
    
    return incide_maximo

array = [7, 7, 6]
maximo = calcular_maximo(array)
print(maximo)

#7 Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
def calcular_maximos(array: list) -> list:
    
    #Encontrar el valor máximo
    maximo = array[0]
    for i in range(1, len(array)):
        if array[i] > maximo:
            maximo = array[i]

    #Contar cuantas veces aparece
    cantidad = 0
    for i in range(len(array)):
        if array[i] == maximo:
            cantidad += 1

    #Crear una lista vacia de ese tamaño
    maximos = [0] * cantidad
    
    #Modificar los valores de dentro por las posiciones
    posicion = 0
    for i in range(len(array)):
        if array[i] == maximo:
            maximos[posicion] = i
            posicion += 1
    
    return maximos

array = [7, 7, 6]
maximos = calcular_maximos(array)
print(maximos)

#8 Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
def reemplazar_nombres(lista_nombres: list, nombre_antiguo: str, nombre_nuevo: str) -> list:
    reemplazos = 0
    
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            reemplazos += 1
    
    return reemplazos
    
array_nombres = ["pepe", "juan", "pedro", "juan"]
reemplazos = reemplazar_nombres(array_nombres, "juan", "bauti")
print(reemplazos)
print(array_nombres)

#9 Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.
def encontrar_interseccion(array: list, array_dos: list) -> list:
    
    contador = 0
    
    #contamos los elementos en comun
    for i in range(len(array)):
        for j in range(len(array_dos)):
            if array[i] == array_dos[j]:
                contador += 1
    
    #creamos el array del tamaño de la interseccion
    interseccion = [0] * contador
    posicion = 0
    
    #Añadimos las intersecciones
    for i in range(len(array)):
        for j in range(len(array_dos)):
            if array[i] == array_dos[j]:
                interseccion[posicion] = array[i]
                posicion += 1
    
    return interseccion

array = [1, 2, 3, 4]
array_dos = [3, 4, 5, 6]

interseccion = encontrar_interseccion(array, array_dos)
print(interseccion)

#10 Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.
def encontrar_union(array: list, array_dos: list) -> list:
    
    union_inicial = [False] * (len(array) + len(array_dos))
    posicion = 0
    
    #Añadimos todos los elementos del array
    for i in range(len(array)):
        union_inicial[posicion] = array[i]
        posicion += 1
    
    #Añadimos los elementos restantes que no estan en union_inicial
    for i in range(len(array_dos)):
        bandera = False
        for j in range(len(array)):
            if array_dos[i] == union_inicial[j]:
                bandera = True
                break
        
        if bandera == True:
            union_inicial[posicion] = array_dos[i]
            posicion += 1
    
    #Recortar array
    #Añadimos los elementos al nuevo array
    union = [False] * posicion
    for i in range(posicion):
        union[i] = union_inicial[i]
        
    return union

array = [1, 2, 3, 4]
array_dos = [3, 4, 5, 6]

union = encontrar_union(array, array_dos)
print(union)

#11 Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.
def encontrar_diferencia(array: list, array_dos: list) -> list:


    diferencia_inicial  = [False] * len(array)
    posicion = 0

    #Cargo el array
    for i in range(len(array)):
        bandera = True

        for j in range(len(array_dos)):
            #compara el elemento en el indice i con todos los elementos del array_dos. En caso de que haya uno repetido no se agrega a la diferencia.
            if array[i] == array_dos[j]:
                bandera = False
                break
            
        if bandera == True:
            diferencia_inicial[posicion] = array[i]
            posicion += 1
            
    # Creamos el array a devolver con las posiciones correspondientes
    diferencia = [False] * posicion

    # Añadimos los elementos válidos al nuevo array
    posicion = 0
    for i in range(len(diferencia)):
        if diferencia_inicial[i] != False:
            diferencia[posicion] = diferencia_inicial[i]
            posicion += 1
            
    return diferencia

array = [1, 2, 3, 4]
array_dos = [3, 4, 5, 6]

diferencia = encontrar_diferencia(array, array_dos)
print(diferencia)