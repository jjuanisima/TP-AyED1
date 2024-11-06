'''
Escribir una función buscarclave() que reciba como parámetros un diccionario y un 
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el dic
cionario. Comprobar el comportamiento de la función mediante un programa apro
piado.
'''


def buscarclave(diccionario: dict, valor: int) -> list:
    '''
    Busca pilotos en el diccionario que tengan la cantidad de campeonatos especificada

    Pre:
        diccionario (dict): un diccionario que asocia pilotos con sus campeonatos
        valor (int): número de campeonatos a buscar
    Post:
        una lista de pilotos (claves) que coinciden con el valor
    '''

    resultado = []
    for piloto, titulo in diccionario.items():
        if titulo == valor:
            resultado.append(piloto)
    return resultado

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    diccionario = {
        'schumacher': 7, 'hamilton': 7,
        'fangio': 5,
        'prost': 4, 'vettel': 4,
        'brabham': 3, 'stewart': 3, 'lauda': 3, 'piquet': 3, 'senna': 3, 'verstappen': 3,
        'ascari': 2, 'g. hill': 2, 'clark': 2, 'fittipaldi': 2, 'hakkinen': 2, 'alonso': 2,
        'farina': 1, 'hawthorn': 1, 'p. hill': 1, 'surtees': 1, 'hulme': 1, 'rindt': 1, 'hunt': 1, 'andretti': 1, 'scheckter': 1, 'jones': 1, 'k. rosberg': 1, 'mansell': 1, 'd. hill': 1, 'villeneuve': 1, 'raikkonen': 1, 'button': 1, 'n. rosberg': 1
    }

    try:
        valor = int(input("Valor a buscar: "))
        resultado = buscarclave(diccionario, valor)
        if resultado:
            for piloto in resultado:
                campeonatos = diccionario[piloto]
                print(f"{piloto}: {campeonatos} campeonatos")
        else:
            print("Ningún piloto tiene ese número de campeonatos :(")
    except ValueError:
        print("ERROR. Revisa de ingresar un número válido :|")
    
main()