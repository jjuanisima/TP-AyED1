'''
Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro 
de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los 
caracteres de la subcadena no necesariamente deben estar en forma consecutiva 
dentro de la cadena, pero sí respetando el orden de los mismos.
'''


def contar_subcadena(cadena: str, subcadena: str) -> str:
    '''
    Revisa cuántas veces aparece una subcadena en la cadena principal

    Pre:
        cadena (str): la cadena principal
        subcadena (str): la subcadena a buscar en la cadena principal
    Post:
        str: cuántas veces aparece la subcadena dentro de la cadena
    '''

    cadena = cadena.lower()
    subcadena = subcadena.lower()

    palabras = cadena.split()
    cant_apariciones = 0

    for palabra in palabras:
        if subcadena == palabra:
            cant_apariciones += 1
    return f"'{subcadena}' aparece {cant_apariciones} veces en la cadena."

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa
    '''
    cadena = "La vaca Lola tiene cabeza y tiene lola"
    subcadena = "Lola"
    print(contar_subcadena(cadena, subcadena))

main()