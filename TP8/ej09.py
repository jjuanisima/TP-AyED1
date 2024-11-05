'''
Escribir un programa que permita ingresar un número entero N y genere un 
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la 
tabla de multiplicar con el formato apropiado.
'''


def tabla_multiplicar(n: int) -> dict:
    '''
    Genera una tabla de multiplicar para un número dado

    Pre:
        n (int): número entero del cual se quiere generar la tabla de multiplicar
    Post:
        devuelve un diccionario donde las claves son los números del 1 al 12 y los valores son los resultados de multiplicar n por esas claves
    '''

    diccionario = {i: n * i for i in range(1, 13)}
    return diccionario

def mostrar_tabla(tabla: dict, n: int) -> None:
    '''
    Printea la tabla de multiplicar en un formato más legible

    Pre:
        tabla (dict): el diccionario que contiene la tabla de multiplicar
        n (int): el número del cual se muestra la tabla
    Post:
        la función no devuelve ningún valor, sólo imprime la tabla
    '''

    for multiplo, resultado in tabla.items():
        print(f"{n} x {multiplo} = {resultado}")

def main() -> None:
    '''
    Función principal, donde se solicita un número al usuario para mostrar su tabla de multiplicar

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    try:
        n = int(input("Número entero: "))
        tabla = tabla_multiplicar(n)
        print(mostrar_tabla(tabla, n))
    except ValueError:
        print("ERROR. Revisa de ingresar un número entero :|")

main()