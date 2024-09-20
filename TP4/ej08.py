'''
Desarrollar una función que devuelva una subcadena con los últimos N caracteres 
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
'''

def subcadena(cadena: str, n: int) -> str:
    '''
    Devuelve una subcadena con los últimos N caracteres de la cadena

    Pre:
        cadena (str): la cadena ingresada por el usuario
        n (int): la cantidad de caracteres de la subcadena
    Post:
        str: una subcadena que contiene los últimos N caracteres de la cadena original
    '''

    return cadena[-n:]

def main() -> None:
    '''
    Función principal, donde el usuario ingresa una cadena y un número N
    '''

    try:
        cadena = input("Cadena: ")
        n = int(input("Valor de N: "))
        print(subcadena(cadena, n))
    except ValueError:
        print("ERROR. Revisa que N sea un número entero.")
    return None

main()