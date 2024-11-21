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
        devuelve una lista con entre 10 y 99 números enteros aleatorios de cuatro dígitos
    '''

    return [rn.randint(1000, 9999) for _ in range(rn.randint(10, 99))]

def calcular_producto(lista: list) -> int:
    '''
    Calcula el producto de todos los elementos de la lista

    Pre:
        lista (list): la lista de la cual multiplicar sus elementos
    Post:
        devuelve el producto de todos los números de la lista
    '''

    producto = 1
    for num in lista:
        producto *= num
    return producto

def eliminar_valor(lista: list, valor: int) -> list:
    '''
    Elimina todas las apariciones de un valor en la lista

    Pre:
        lista (list): la lista de la cual eliminar el valor
        valor (int): el valor a eliminar
    Post:
        devuelve la lista sin el valor
    '''

    while valor in lista:
        lista.remove(valor)
    return lista

def es_capicua(lista_final: list) -> bool:
    '''
    Evalúa si el contenido de la lista es capicúa

    Pre:
        lista_final (list): la lista a revisar
    Post:
        devuelve True si la lista es capicúa, en caso contrario False
    '''

    return lista_final == lista_final[::-1]

if __name__ == "__main__":
    lista = cargar_lista()
    print(f"Lista: {lista}")
    producto = calcular_producto(lista)
    print(f"Producto de todos los elementos de la lista: {producto}")
    
    try:
        valor = int(input("\nValor a encontrar: "))
    except ValueError:
        print("ERROR. Revisa de ingresar un número entero válido :|")
    else:
        lista_final = eliminar_valor(lista, valor)
        print(f"Lista final: {lista_final}")

        if es_capicua(lista_final):
            print("\nLa lista es capicúa :)")
        else:
            print("\nLa lista no es capicúa :(")