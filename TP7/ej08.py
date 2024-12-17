'''
Realizar la implementación recursiva del método de selección para ordenar una lista
de números enteros. Sugerencia: Colocar el elemento más pequeño en la primera
posición, y luego ordenar el resto de la lista con una llamada recursiva. No usar las
funciones min() ni max() de Python
'''


from typing import List

def ordenar_lista(lista: List[int], izq=0) -> List[int]:
    '''
    Ordena la lista intercambiando los números de acuerdo a si el de la izquierda es mayor que el de la derecha

    Pre:
        lista (List[int]): la lista de elementos a ordenar
        izq (int): el índice actual que se está evaluando en la lista, arrancando en 0
    Post:
        devuelve la lista ordenada
    '''

    if izq == len(lista) - 1:
        return lista
    
    if lista[izq] > lista[izq+1]:
        aux = lista[izq]
        lista[izq] = lista[izq+1]
        lista[izq+1] = aux
        return ordenar_lista(lista, izq-1)
    else:
        return ordenar_lista(lista, izq+1)

if __name__ == "__main__":
    lista = [1, 33, 77, 55, 99, 22, 66, 44, 88]
    print(f"Lista original: {lista}")
    resultado = ordenar_lista(lista, izq=0)
    print(f"Lista ordenada: {resultado}")