'''
Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas 
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True 
o False. Escribir también un programa para verificar su comportamiento. Considerar 
el uso de conjuntos para resolver este ejercicio.
'''


def encajan_fichas(ficha1: tuple, ficha2: tuple) -> bool:
    '''
    Determina si dos fichas de dominó encajan, o sea si ambas fichas tienen un número en común

    Pre:
        ficha1 (tuple): una tupla con dos números, la primera ficha
        ficha2 (tuple): una tupla con dos números, la segunda ficha
    Post:
        devuelve True si las fichas encajan, False en caso contrario
    '''

    return not set(ficha1).isdisjoint(set(ficha2))

def main() -> bool:
    '''
    Función principal, donde se evalúa si dos fichas de dominó encajan

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    ficha1 = (3, 4)
    ficha2 = (5, 4)

    if encajan_fichas(ficha1, ficha2):
        print(f"Las fichas {ficha1} y {ficha2} encajan :)")
    else:
        print(f"Las fichas {ficha1} y {ficha2} no encajan :(")

main()