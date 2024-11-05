'''
Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales 
contiene, identificando la cantidad de cada una. Devolver un diccionario con los 
resultados. Luego desarrollar un programa para leer una frase e invocar a la 
función por cada palabra que contenga la misma. Imprimir las palabras y la 
cantidad de vocales hallada.
'''


def contarvocales(palabra: str) -> dict:
    '''
    Cuenta la cantidad de veces que aparece cada vocal en una palabra

    Pre:
        palabra (str): la palabra en la que se van a contar las vocales
    Post:
        un diccionario con la cantidad de veces que aparece cada vocal en la palabra
    '''

    cant_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    palabra = palabra.lower()

    for letra in palabra:
        if letra in cant_vocales:
            cant_vocales[letra] += 1
    return cant_vocales

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    palabra = "Pastafrola"
    resultado = contarvocales(palabra)
    print(f"Cantidad total de vocales:")
    for vocal, cantidad in resultado.items():
        print(f"{vocal}: {cantidad}")

main()