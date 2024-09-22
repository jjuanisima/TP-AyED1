'''
Las siguientes matrices responden distintos patrones de relleno. Desarrollar funcio
nes que generen cada una de ellas sin intervención humana y escribir un programa 
que las invoque e imprima por pantalla. El tamaño de las matrices debe estable
cerse como N x N, donde N se ingresa a través del teclado.
'''

def matriz_a(n: int) -> list:
    '''
    Crea una matriz de N * N con números impares crecientes en la diagonal

    Pre:
        n (int): valor de n, que define el tamaño de la matriz
    Post:
        matriz (list): la matriz con los elementos modificados
    '''
    
    matriz = [[0] * n for i in range(n)]
    num_impar = 1
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                matriz[i][j] = num_impar
                num_impar += 2
    return matriz

def matriz_b(n: int) -> list:
    '''
    Crea una matriz de N * N con potencias decrecientes de 3 en la diagonal inversa

    Pre:
        n (int): valor de n, que define el tamaño de la matriz
    Post:
        matriz (list): la matriz con los elementos modificados
    '''

    matriz = [[0] * n for i in range(n)]
    num = (3 ** (n - 1))
    for i in range(len(matriz)):
        matriz[i][n-1-i] = num
        num //= 3
    return matriz

def matriz_c(n: int) -> list:
    '''
    Crea una matriz de N * N con números decrecientes en la diagonal principal y debajo de ella

    Pre:
        n (int): valor de n, que define el tamaño de la matriz
    Post:
        matriz (list): la matriz con los elementos modificados
    '''

    matriz = [[0] * n for i in range(n)]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j or i > j:
                matriz[i][j] = n - i
    return matriz

def matriz_d(n: int) -> list:
    '''
    Crea una matriz de N * N con potencias decrecientes de 2 en cada fila

    Pre:
        n (int): valor de n, que define el tamaño de la matriz
    Post:
        matriz (list): la matriz con los elementos modificados
    '''

    matriz = [[(2 ** (n - 1) // (2 ** i))] * n for i in range(n)]
    return matriz

def matriz_e(n: int) -> list:
    '''
    Crea una matriz de N * N con ceros intercalados con números crecientes

    Pre:
        n (int): valor de n, que define el tamaño de la matriz
    Post:
        matriz (list): la matriz con los elementos modificados
    '''

    matriz = [[0] * n for i in range(n)]
    num = 1
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (i + j) % 2 != 0:
                matriz[i][j] = num
                num += 1
    return matriz

def matriz_f(n: int) -> list:
    '''
    Crea una matriz de N * N con números consecutivos en la diagonal inversa y abajo de ella

    Pre:
        n (int): valor de n, que define el tamaño de la matriz
    Post:
        matriz (list): la matriz con los elementos modificados
    '''
    
    matriz = [[0] * n for i in range(n)]
    num = 1
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j or i > j:
                matriz[i][n-1-j] = num
                num += 1
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

    print("\nMatriz b:")
    printear_matriz(matriz_b(n))

    print("\nMatriz c:")
    printear_matriz(matriz_c(n))

    print("\nMatriz d:")
    printear_matriz(matriz_d(n))

    print("\nMatriz e:")
    printear_matriz(matriz_e(n))

    print("\nMatriz f:")
    printear_matriz(matriz_f(n))

main()