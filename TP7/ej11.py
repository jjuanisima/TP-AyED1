'''
Desarrollar una función que devuelva el mínimo elemento de una matriz de M x N
'''


from typing import List

def buscar_minimo(matriz: List[List[int]], fila=0, minimo=None) -> int:
    '''
    Busca el mínimo elemento en una matriz de enteros, evaluando fila por fila el menor elemento

    Pre:
        matriz (List[List[int]]): una matriz de enteros
        fila (int): el índice de la fila que se está evaluando, arrancando en 0
        minimo (int o None): el valor mínimo encontrado hasta el momento. Arranca en None y en cada pasada se actualiza
    Post:
        devuelve el valor mínimo encontrado en toda la matriz
    '''

    if fila >= len(matriz):
        return minimo
    
    minimo_fila = min(matriz[fila])
    
    if minimo is None or minimo_fila < minimo:
        minimo = minimo_fila

    return buscar_minimo(matriz, fila+1, minimo)

if __name__ == "__main__":
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    resultado = buscar_minimo(matriz, fila=0, minimo=None)
    print(f"El mínimo elemento de la matriz es {resultado}")