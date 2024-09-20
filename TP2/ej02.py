'''
Escribir funciones para:
    a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa 
a través del teclado.
    b. Recibir una lista como parámetro y devolver True si la misma contiene algún 
elemento repetido. La función no debe modificar la lista.
    c. Recibir una lista como parámetro y devolver una nueva lista con los elementos 
únicos de la lista original, sin importar el orden. 
Combinar estas tres funciones en un mismo programa.
'''


import random as rn

def cargar_lista(valor) -> list:
    '''
    Carga la lista con n cantidad de números aleatorios entre 1 y 100

    Pre:
        valor (int): cantidad de números que va a tener la lista
    Post:
        lista (list): lista cargada con los números
    '''

    for i in range(valor):
        lista.append(rn.randint(1, 100))
    return lista

def buscar_elemento_compartido(lista_random) -> bool:
    '''
    Revisa si un elemento de la lista original se repite en la otra lista

    Pre:
        lista_random (list): otra lista con la que comparar la original
    Post:
        true: las listas tienen al menos un elemento compartido
        false: las listas no comparten ningún elemento
    '''

    for i in range(len(lista)):
        if lista[i] in lista_random:
            return True
    return False

def lista_elementos_unicos(lista, lista_random) -> list:
    '''
    Crea una lista con los elementos únicos de la lista original

    Pre:
        lista (list): la lista original
        lista_random (list): otra lista con la que comparar la original
    Post:
        lista_originales (list): lista con los números únicos
    '''
    lista_originales = []
    for i in range(len(lista)):
        if lista[i] not in lista_random:
            lista_originales.append(lista[i])
    return lista_originales

def main() -> None:
    '''
    Función principal, donde el usuario ingresa la cantidad de números que tendrá la lista
    '''
    
    try:
        valor = int(input("Cantidad de números de la lista: "))
        print(cargar_lista(valor))
        print(buscar_elemento_compartido(lista_random))
        print(lista_elementos_unicos(lista, lista_random))
    except ValueError:
        print("ERROR. Revisa que el número sea un entero.")
    return None

lista = []
lista_random = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

main()