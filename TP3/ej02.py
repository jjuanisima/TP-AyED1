'''
Las siguientes matrices responden distintos patrones de relleno. Desarrollar funcio
nes que generen cada una de ellas sin intervención humana y escribir un programa 
que las invoque e imprima por pantalla. El tamaño de las matrices debe estable
cerse como N x N, donde N se ingresa a través del teclado.
'''

def matriz_a(n: int) -> list:
    '''
    Crea una matriz de N * N con números impares en la diagonal y ceros en las demás posiciones

    Pre:
        n (int): valor de n, que define el tamaño de la matriz
    Post:
        matriz (list): la matriz con ceros y números impares en diagonal
    '''
    
    matriz = [[0] * n for i in range(n)]
    num_impar = 1
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                matriz[i][j] = num_impar
                num_impar += 2
    return matriz

def printear_matriz(matriz: list) -> None:
    '''
    Printea las matrices
    '''

    for fila in matriz:
        print(fila)

def main() -> None:
    '''
    Función principal, donde el usuario ingresa el valor de n y se ejecuta el programa
    '''

    n = int(input("Valor de N (tamaño de la matriz): "))

    print("\nMatriz a:")
    printear_matriz(matriz_a(n))

main()