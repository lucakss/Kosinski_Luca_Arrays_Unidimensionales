def ingresar_datos() -> list:
    
    contador = 0
    lista = [False] * 10
    
    while contador < 10:
        
        for i in range(len(lista)):
            numero = int(input("Ingrese un numero entero entre -1000 y 1000: "))
            if numero < -1000 or numero > 1000:
                print("No ingresaste un numero valido")
                continue
            
            lista[i] = numero
            contador += 1
            
        return lista

def calcular_positivos_negativos(lista: list) -> None:

    positivos = 0
    negativos = 0
    
    for i in range(len(lista)):
        if lista[i] > 0:
            positivos += 1
            
        elif lista[i] < 0:
            negativos += 1
            
    print(f"Se ingresaron {positivos} positivos y {negativos} negativos")

def determinar_par_impar(numero: int) -> bool:
        if numero % 2 == 0:
            return True
        return False
    
def determinar_mayor_impar(lista: list) -> None:
    mayor_impar = lista[0]
    
    for i in range(len(lista)):
        if not determinar_par_impar(lista[i]):
            if lista[i] > mayor_impar:
                mayor_impar = lista[i]
        
    print(f"El mayor numero impar es {mayor_impar}")            