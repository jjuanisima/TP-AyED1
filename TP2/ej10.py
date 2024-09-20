'''
Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los 
elementos de la primera que sean impares. El proceso deberá realizarse utilizando 
la función filter(). Imprimir las dos listas por pantalla.
'''


import random as rn

lista = [rn.randint(1, 100) for i in range(20)]

lista_impares = list(filter(lambda i: i % 2 != 0, lista))

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa
    '''
    print(lista)
    print(lista_impares)
    return None

main()