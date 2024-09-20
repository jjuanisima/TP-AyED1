'''
Desarrollar un programa para rellenar una matriz de N x N con números enteros al 
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repi
ta. Imprimir la matriz por pantalla.
'''


import random as rn

def crear_matriz(n: int) -> list:
    '''
    Creo una matriz de N * N con números random entre 0 y N**2

    Pre:
        n (int): valor de n, que define el tamaño de la matriz
    Post:
        matriz (list): la matriz con números random
    '''

    matriz = [[rn.randint(1, n**n) for j in range(n)] for i in range(n)]
    '''
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(rn.randint(1, n**n))
        matriz.append(fila)
    return matriz
    '''

def printear_matriz(matriz: list) -> None:
    '''
    Printea la matriz por fila
    '''

    for fila in matriz:
        print(fila)

def main() -> None:
    '''
    Función principal, donde el usuario ingresa el valor de N y se ejecuta el programa
    '''
    
    n = int(input("Valor de N: "))
    matriz = crear_matriz(n)
    printear_matriz(matriz)
    return None

main()
# pancho