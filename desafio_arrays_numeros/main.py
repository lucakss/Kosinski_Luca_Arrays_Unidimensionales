from Especificas import *
from Array_Generales import *

def mostrar_menu() -> None:
    print("-------------------------------")
    print("1 - Cantidad de positivos y negativos")
    print("2 - Suma de numeros pares")
    print("3 - Mayor numero impar")
    print("4 - Listar numeros ingresados")
    print("5 - Listar numeros pares")
    print("6 - Listar numeros en posiciones impares")
    print("7 - Salir")
    print("-------------------------------\n")
    eleccion = int(input("Elige un numero: "))
    
    return eleccion

def mostrar_eleccion(eleccion: int = 0) -> None:
    while eleccion != 7:
        eleccion = mostrar_menu()
        if eleccion == 1:
            calcular_positivos_negativos(datos)
        elif eleccion == 2:
            sumar_pares(datos)
        elif eleccion == 3:
            determinar_mayor_impar(datos)
        elif eleccion == 4:
            mostrar_numeros_ingresados(datos)
        elif eleccion == 5:
            mostrar_numeros_pares(datos)
        elif eleccion == 6:
            mostrar_numeros_indices_impares(datos)
        elif eleccion == 7:
            print("Adios")
            eleccion = 7
            
datos = ingresar_datos()
mostrar_eleccion()