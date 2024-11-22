'''
Escribir una función que sume todos los elementos de una matriz de M x N y de
vuelva el resultado. No usar la función sum()
'''

def sumar_numeros(matriz: list) -> int:
    '''
    Suma los números de la matriz

    Pre:
        matriz (list): la matriz que contiene los números a sumar
    Post:
        devuelve el resultado de la suma de los elementos de la matriz
    '''

    if not matriz:
        return 0
    else:
        for fila in matriz:
            suma_fila = 0
            for num in fila:
                suma_fila += num
            return suma_fila + (sumar_numeros(matriz[1:]))
            
if __name__ == "__main__":
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    resultado = sumar_numeros(matriz)
    print(f"Resultado: {resultado}")