'''
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
verificar su funcionamiento.
'''


def es_capicua(cadena) -> bool:
    '''
    Revisa si la cadena ingresada es capicúa

    Pre:
        cadena (str): la cadena a evaluar
    Post:
        false: la cadena no es capicúa
        true: la cadena es capicúa
    '''
    
    inicio = 0
    fin = len(cadena) - 1

    while inicio < fin:
        if cadena[inicio] != cadena[fin]:
            return False
        inicio += 1
        fin -= 1
    return True

def main() -> None:
    '''
    Función principal, donde el usuario ingresa una cadena y se ejecuta el programa
    '''

    cadena = input("Ingrese una cadena de caracteres: ")

    if es_capicua(cadena):
        print(f"{cadena} es capicúa :)")
    else:
        print(f"{cadena} no es capicúa :(")
    return None

main()