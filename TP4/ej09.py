'''
Escribir una función que reciba como parámetro una cadena de caracteres en la que 
las palabras se encuentran separadas por uno o más espacios. Devolver otra 
cadena con las palabras ordenadas según su longitud, dejando un espacio entre 
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la 
longitud de las palabras, pero deberán conservarse en la cadena final.
'''

def ordenar_palabras(cadena: str) -> str:
    '''
    Crea una cadena con las palabras de la cadena principal, ordenándolas según su longitud y dejando espacio entre ellas

    Pre:
        cadena (str): la cadena principal
    Post:
        str: retorna la cadena nueva
    '''

    palabras = cadena.split()

    palabras_ordenadas = []

    while palabras:
        palabra_menor = palabras[0]
        for palabra in palabras:
            if len(palabra) < len(palabra_menor):
                palabra_menor = palabra

        palabras_ordenadas.append(palabra_menor)
        palabras.remove(palabra_menor)

    resultado = ""
    for palabra in palabras_ordenadas:
        resultado += palabra + " "

    return resultado
    
def main() -> None:
    '''
    Función principal, donde se ejecuta el programa
    '''

    cadena = "La vaca Lola tiene cabeza y tiene cola"
    print(ordenar_palabras(cadena))

main()