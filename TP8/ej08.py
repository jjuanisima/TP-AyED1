'''
Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
'''


def generar_diccionario() -> dict:
    '''
    Genera un diccionario donde las claves son números del 1 al 20 y los valores son sus cuadrados

    Pre:
        la función no recibe parámetros
    Post:
        devuelve un diccionario con la estructura {número: cuadrado}
    '''

    diccionario = {num: num**2 for num in range(1, 21)}
    return diccionario

def main() -> None:
    '''
    Función principal, donde se imprime el diccionario generado

    Esta función no recibe parámetros y no devuelve ningún valor
    '''
    
    print(generar_diccionario())

main()