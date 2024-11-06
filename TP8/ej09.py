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

    return {i: n * i for i in range(1, 13)}

def main() -> None:
    '''
    Función principal, donde se solicita un número al usuario para mostrar su tabla de multiplicar

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    try:
        n = int(input("Número entero: "))
        tabla = tabla_multiplicar(n)
        for multiplo, resultado in tabla.items():
            print(f"{n} x {multiplo} = {resultado}")
    except ValueError:
        print("ERROR. Revisa de ingresar un número entero :|")

main()