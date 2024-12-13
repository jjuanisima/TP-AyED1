'''
Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas 
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True 
o False. Escribir también un programa para verificar su comportamiento. Considerar 
el uso de conjuntos para resolver este ejercicio.
'''


def encajan_fichas(ficha1: tuple, ficha2: tuple) -> bool:
    '''
    Determina si dos fichas de dominó encajan, o sea si tienen un número en común

    Pre:
        ficha1, ficha2 (tuple): una tupla con dos números
    Post:
        devuelve True si las fichas encajan, en caso contrario False
    '''

    return not set(ficha1).isdisjoint(set(ficha2))

if __name__ == "__main__":
    ficha1 = (3, 4)
    ficha2 = (5, 4)

    print(f"Las fichas {ficha1} y {ficha2} encajan :)") if encajan_fichas(ficha1, ficha2) else print(f"Las fichas {ficha1} y {ficha2} no encajan :(")