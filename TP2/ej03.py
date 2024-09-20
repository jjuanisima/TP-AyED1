'''
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), 
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valo
res de la lista.
'''


def lista_cuadrados(n) -> list:
    '''
    Carga la lista con los cuadrados de los números entre 1 y n+1 (n ingresado por el usuario)

    Pre:
        n = cantidad de números que va a tener la lista
    Post:
        lista (list): la lista cargada
    '''

    for i in range(1, n+1):
        lista.append(i ** 2)
    return lista

def ultimos_diez(lista) -> list:
    '''
    Lista con los últimos diez elementos de la lista original

    Pre:
        lista (list): la lista original
    Post:
        lista (list): lista cargada con los últimos diez elementos
    '''

    return lista[-10:]

def main() -> None:
    '''
    Función principal, donde el usuario ingresa la cantidad de números que va a tener la lista
    '''
    try:
        n = int(input("Valor de N: "))
        print(lista_cuadrados(n))
        print(ultimos_diez(lista))
    except ValueError:
        print("ERROR. Revisa que N sea un número entero.")
    return None

lista = []

main()