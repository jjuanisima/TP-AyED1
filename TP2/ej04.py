'''
Eliminar de una lista de números enteros aquellos valores que se encuentren en 
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista 
resultante. La función debe modificar la lista original sin crear una copia modificada.
'''


def modificar_lista() -> list:
    '''
    Elimina de lista1 los elementos que se encuentren en lista2

    Pre:
        La función no recibe parámetros
    Post:
        lista1 (list): lista1 sin los números de lista2
    '''

    for num in lista2:
        while num in lista1:
            lista1.remove(num)
    return lista1

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa
    '''
    print(f"Lista original: {lista1}")
    print(f"Valores a eliminar: {lista2}")
    print(f"Lista resultante: {modificar_lista()}")

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [6, 7, 8, 9, 10, 11, 12, 13, 14]

main()