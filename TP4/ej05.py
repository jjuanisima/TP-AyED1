'''
Escribir una función filtrar_palabras() que reciba una cadena de caracteres conte
niendo una frase y un entero N, y devuelva otra cadena con las palabras que ten
gan N o más caracteres de la cadena original. Escribir también un programa para 
verificar el comportamiento de la misma. Hacer tres versiones de la función, para 
cada uno de los siguientes casos:
    a. Utilizando sólo ciclos normales
    b. Utilizando listas por comprensión
    c. Utilizando la función filter
'''


def filtrar_palabras(cadena: str, n: int) -> str:
    '''
    Crea una cadena con las palabras de la cadena que tengan N o más caracteres

    Pre:
        cadena (str): la cadena ingresada por el usuario
        n (int): valor de n, que define la longitud mínima de las palabras a buscar
    Post:
        str: Retorna la cadena de palabras, separadas por espacios
    '''

    palabras = cadena.split()
    resultado = ""

    for palabra in palabras:
        if len(palabra) >= n:
            resultado += palabra + " "
    return resultado

def palabras_ciclos(cadena: str, n: int) -> str:
    '''
    Crea una cadena con las palabras de la cadena que tengan N o más caracteres, usando ciclos normales

    Pre:
        cadena (str): la cadena ingresada por el usuario
        n (int): valor de n, que define la longitud mínima de las palabras a buscar
    
    Post:
        str: Retorna la cadena de palabras, separadas por espacios
    '''

    palabras = cadena.split()
    resultado = []

    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)
    return " ".join(resultado)

def palabras_comprension(cadena: str, n: int):
    '''
    Crea una cadena con las palabras de la cadena que tengan N o más caracteres, usando listas por comprensión

    Pre:
        cadena (str): la cadena ingresada por el usuario
        n (int): valor de n, que define la longitud mínima de las palabras a buscar
    
    Post:
        str: Retorna la cadena de palabras, separadas por espacios
    '''

    palabras = cadena.split()
    resultado = [palabra for palabra in palabras if len(palabra) >= n]
    return " ".join(resultado)

def palabras_filter(cadena: str, n: int):
    '''
    Crea una cadena con las palabras de la cadena que tengan N o más caracteres, usando la función filter()

    Pre:
        cadena (str): la cadena ingresada por el usuario
        n (int): valor de n, que define la longitud mínima de las palabras a buscar
    
    Post:
        str: Retorna la cadena de palabras, separadas por espacios
    '''
    
    palabras = cadena.split()
    resultado = filter(lambda palabra: len(palabra) >= n, palabras)
    return " ".join(resultado)

def main() -> None:
    '''
    Función principal, donde el usuario ingresa una cadena y un número n
    '''

    try:
        cadena = input("Cadena: ")
        n = int(input("Valor de N: "))
        print(filtrar_palabras(cadena, n))
        print(palabras_ciclos(cadena, n))
        print(palabras_comprension(cadena, n))
        print(palabras_filter(cadena, n))
    except ValueError:
        print("ERROR. Revisa que N sea un número entero.")
    return None

main()