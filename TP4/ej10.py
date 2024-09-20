'''
Desarrollar una función para reemplazar todas las apariciones de una palabra por 
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la 
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse 
palabras completas, y no fragmentos de palabras. Escribir también un programa 
para verificar el comportamiento de la función. 
'''


def reemplazar_palabra(cadena: str, palabra_anterior: str, palabra_nueva: str) -> tuple:
    '''
    Reemplaza las apariciones de una palabra por otra en la cadena principal

    Pre:
        cadena (str): la cadena principal
        palabra_anterior (str): la palabra a reemplazar
        palabra_nueva (str): la palabra que reemplaza
    Post:
        resultado, cant_reemplazos (tuple): la cadena con la modificación hecha, y la cantidad de reemplazos que hubo
    '''

    palabras = cadena.split()

    cant_reemplazos = 0

    palabras_modificadas = []

    for palabra in palabras:
        if palabra == palabra_anterior:
            palabras_modificadas.append(palabra_nueva)
            cant_reemplazos += 1
        else:
            palabras_modificadas.append(palabra)

    resultado = ""
    for palabra in palabras_modificadas:
        resultado += palabra + " "

    return resultado, cant_reemplazos

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa
    '''
    
    cadena = "La vaca Lola tiene cabeza y tiene cola"
    palabra_anterior = "Lola"
    palabra_nueva = "Marcelo"

    resultado, cant_reemplazos = reemplazar_palabra(cadena, palabra_anterior, palabra_nueva)

    print(resultado)
    print(cant_reemplazos)

main()