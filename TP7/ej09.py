'''
Realizar una función recursiva para imprimir una matriz de M x N con el formato
apropiado
'''

def printear_matriz(matriz: list, fila: int) -> None:
    '''
    Printea una matriz de M x N

    Pre:
        matriz (list): la matriz a printear
        fila (int): la lista de la matriz (inicia en 0, por índice)
    Post:
        no devuelve nada, sólo printea
    '''

    if fila >= len(matriz):
        return
    print("  ".join(map(str, matriz[fila])))
    return printear_matriz(matriz, fila + 1)

if __name__ == "__main__":
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    fila = 0
    printear_matriz(matriz, fila)