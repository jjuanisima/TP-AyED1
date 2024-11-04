'''
El método index permite buscar un elemento dentro de una lista, devolviendo la 
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se 
produce una excepción de tipo ValueError. Desarrollar un programa que cargue 
una lista con números enteros ingresados a través del teclado (terminando con -1) 
y permita que el usuario ingrese el valor de algunos elementos para visualizar la 
posición que ocupan, utilizando el método index. Si el número no pertenece a la 
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el 
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
'''


from typing import List

def crear_lista(lista: List[int]) -> List[int]:
    '''
    Carga la lista con números ingresados por el usuario, finalizando la carga al ingresar -1

    Pre:
        lista (list): la lista a cargar
    Post:
        devuelve la lista cargada
    '''

    while True:
        try:
            num = int(input("Ingrese un número: "))
            if num == -1:
                break
        except ValueError:
            print("ERROR. Revisa de ingresar un número entero :|\n")
        else:
            lista.append(num)
    return lista

def posicion_numeros(lista_final: List[int]) -> None:
    '''
    Busca la posición en la lista del número ingresado por el usuario. En caso de no encontrarse se muestra un mensaje de error, y a los tres errores el programa se detiene

    Pre:
        lista_final (list): la lista previamente cargada, donde vamos a buscar el índice del número deseado
    Post:
        la función no devuelve ningún valor
    '''

    cant_intentos = 0

    while cant_intentos < 3:
        try:
            num_a_buscar = int(input("\nNúmero a buscar su índice en la lista: "))
            posicion = lista_final.index(num_a_buscar)
            print(f"El número {num_a_buscar} está en la posición {posicion + 1} :)")
        except ValueError:
            cant_intentos += 1
            print(f"ERROR. No se encontró el número {num_a_buscar} en la lista :(")
            if cant_intentos >= 3:
                print("Demasiados intentos fallidos, saliendo...")
                break

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    lista = []
    lista_final = crear_lista(lista)
    posicion_numeros(lista_final)

main()