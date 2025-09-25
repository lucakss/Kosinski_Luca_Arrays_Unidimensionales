from Especificas import determinar_par_impar

def sumar_pares(lista: list) -> int:
    suma_pares = 0
    
    for i in range(len(lista)):
        if determinar_par_impar(lista[i]):
            suma_pares += lista[i]
    print(f"La suma de los pares es {suma_pares}")
            
def mostrar_numeros_ingresados(lista: list) -> None:
    for i in range(len(lista)):
        print(lista[i])

def mostrar_numeros_pares(lista: list) -> None:
    for i in range(len(lista)):
        if determinar_par_impar(lista[i]):
            print(f"{lista[i]} es par")
            
def mostrar_numeros_indices_impares(lista: list) -> None:
    for i in range(len(lista)):
        if not determinar_par_impar(i):
            print(f"{lista[i]} su indice es impar")
    

