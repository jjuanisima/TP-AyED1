'''
Escribir una función que reciba una lista como parámetro y devuelva True si la lista 
está ordenada en forma ascendente o False en caso contrario. Por ejemplo, 
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar 
además un programa para verificar el comportamiento de la función. 
'''


def esta_ordenada(lista) -> bool:
    '''
    Revisa si la lista está ordenada

    Pre:
        lista (list): la lista a evaluar
    Post:
        true: la lista está ordenada
        false: la lista no está ordenada
    '''

    for i in range(len(lista) - 1):
        if lista[i+1] > lista[i]:
            return True
    return False

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa
    '''
    
    print(esta_ordenada(lista))
    return None

lista = [5, 4, 3, 2, 1]

main()