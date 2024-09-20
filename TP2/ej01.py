'''
Desarrollar cada una de las siguientes funciones y escribir un programa que per
mita verificar su funcionamiento imprimiendo la lista luego de invocar a cada fun
ción:
    a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elemen
tos también será un número al azar de dos dígitos.
    b. Calcular y devolver el producto de todos los elementos de la lista anterior.
    c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar 
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar 
listas auxiliares.
    d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas 
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
'''


import random as rn

def cargar_lista() -> list:
    '''
    Carga una lista con números al azar de cuatro dígitos

    Pre:
        La función no recibe parámetros
    Post:
        lista (list): lista con entre 10 y 99 números enteros aleatorios de cuatro dígitos
    '''

    for i in range(rn.randint(10, 99)):
        lista.append(rn.randint(1000, 9999))
    return lista

def calcular_producto() -> int:
    '''
    Calcula el producto de todos los elementos de la lista

    Pre:
        La función no recibe parámetros
    Post:
        producto (int): el producto de todos los números de la lista
    '''

    producto = 1
    for i in range(len(lista)):
        producto *= lista[i]
    return producto

def eliminar_valor(valor) -> list:
    '''
    Elimina todas las apariciones de un valor en la lista

    Pre:
        valor (int): el valor a eliminar
    Post:
        lista (list): la lista sin el valor
    '''

    for i in range(len(lista)):
        if valor in lista:
            lista.remove(valor)
    return lista

def es_capicua(lista) -> bool:
    '''
    Evalúa si el contenido de la lista es capicúa

    Pre:
        lista (list): la lista a revisar
    Post:
        false: la lista no es capicúa
        true: la lista es capicúa
    '''

    for num in lista:
        num_str = str(num)
        if num_str != num_str[::-1]:
            return False
    return True

def main() -> None:
    '''
    Función principal, donde el usuario ingresa un valor a encontrar
    '''
    
    valor = int(input("Valor a encontrar: "))
    print(cargar_lista())
    print(calcular_producto())
    print(eliminar_valor(valor))

    if es_capicua(lista):
        print("La lista es capicúa :)")
    else:
        print("La lista no es capicúa :(")

lista = []

main()