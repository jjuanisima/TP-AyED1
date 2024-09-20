'''
Escribir una función para eliminar una subcadena de una cadena de caracteres, a 
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resul
tante. Escribir también un programa para verificar el comportamiento de la misma. 
Escribir una función para cada uno de los siguientes casos:
    a. Utilizando rebanadas
    b. Sin utilizar rebanadas
'''


def subcadena_rebanadas(cadena: str, posicion: int, caracteres: int) -> str:
    '''
    Elimina una subcadena de una cadena principal, usando rebanadas

    Pre:
        cadena (str): la cadena ingresada por el usuario
        posicion (int): posición donde comienza la subcadena
        caracteres (int): cantidad de caracteres de la subcadena
    Post:
        subcadena (str): la cadena resultante sin la subcadena eliminada
    '''

    subcadena = cadena[:posicion] + cadena[posicion+caracteres:]
    return subcadena

def subcadena_sin_rebanadas(cadena: str, posicion: int, caracteres: int) -> str:
    '''
    Elimina una subcadena de una cadena principal, sin usar rebanadas

    Pre:
        cadena (str): la cadena ingresada por el usuario
        posicion (int): posición donde comienza la subcadena
        caracteres (int): cantidad de caracteres de la subcadena
    Post:
        subcadena (str): la cadena resultante sin la subcadena eliminada
    '''

    subcadena = ""
    for i in range(len(cadena)):
        if i < posicion or i >= posicion + caracteres:
            subcadena += cadena[i]
    return subcadena

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa
    '''
    cadena = "El número de teléfono es 4356 7890"
    posicion = 25
    caracteres = 9
    print(subcadena_rebanadas(cadena, posicion, caracteres))
    print(subcadena_sin_rebanadas(cadena, posicion, caracteres))

main()
