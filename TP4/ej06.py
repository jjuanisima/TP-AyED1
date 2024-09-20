'''
Desarrollar una función que extraiga una subcadena de una cadena de caracteres, 
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena 
como valor de retorno. Escribir también un programa para verificar el comporta
miento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres, 
resultando la subcadena "4356-7890". Escribir una función para cada uno de los si
guientes casos:
    a. Utilizando rebanadas
    b. Sin utilizar rebanadas
'''


def subcadena_rebanadas(cadena: str, posicion: int, caracteres: int) -> str:
    '''
    Extrae una subcadena de una cadena, dependiendo de la posición y la cantidad de caracteres deseada, usando rebanadas

    Pre:
        cadena (str): la cadena ingresada por el usuario
        posicion (int): posición donde comienza la subcadena
        caracteres (int): cantidad de caracteres de la subcadena
    Post:
        subcadena (str): la subcadena extraída de la cadena principal
    '''

    subcadena = cadena[posicion:posicion + caracteres]
    return subcadena

def subcadena_sin_rebanadas(cadena: str, posicion: int, caracteres: int) -> str:
    '''
    Extrae una subcadena de una cadena, dependiendo de la posición y la cantidad de caracteres deseada, sin usar rebanadas

    Pre:
        cadena (str): la cadena ingresada por el usuario
        posicion (int): posición donde comienza la subcadena
        caracteres (int): cantidad de caracteres de la subcadena
    Post:
        subcadena (str): la subcadena extraída de la cadena principal
    '''

    subcadena = ""
    for i in range(posicion, posicion+caracteres):
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