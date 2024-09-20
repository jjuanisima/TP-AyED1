'''
Escribir una función que reciba una lista de números enteros como parámetro y la 
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las pro
porciones relativas que cada elemento tiene en la lista original. Desarrollar también 
un programa que permita verificar el comportamiento de la función. Por ejemplo, 
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
'''


def normalizar(lista) -> list:
    '''
    Recibe una lista de enteros y devuelve una lista normalizada, donde los elementos suman 1.0
    
    Pre:
        lista (list): lista a normalizar
    Post:
        lista_normalizada (list): lista normalizada
    '''
    
    total = sum(lista)

    lista_normalizada = []
    for num in lista:
        lista_normalizada.append(num / total)
    return lista_normalizada

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa
    '''

    print(normalizar(lista))

lista = [1, 1, 2]

main()