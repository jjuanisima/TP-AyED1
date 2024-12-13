'''
Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras 
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras 
ordenadas según su longitud. Los signos de puntuación no deben afectar el 
proceso.
'''


import re

def arreglar_frase(frase: str) -> list:
    '''
    Elimina los signos de puntuación de la frase y devuelve una lista con las palabras únicas, ordenadas por su longitud

    Pre:
        frase (str): la frase de entrada
    Post:
        una lista de palabras únicas ordenadas por longitud
    '''

    sin_puntuacion = re.findall(r'[a-zA-Z0-9]+', frase)

    palabras = set(sin_puntuacion)

    palabras_ordenadas = sorted(palabras, key=len)

    return palabras_ordenadas

if __name__ == "__main__":
    frase = input("Frase: ")
    
    frase_final = arreglar_frase(frase)

    print("Palabras únicas ordenadas por longitud:")
    for palabra in frase_final:
        print(palabra)