'''
Escribir un programa para crear una lista por comprensión con los naipes de la ba
raja española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2 
Oros"... ]. Imprimir la lista por pantalla. 
'''


def crear_lista() -> list:
    '''
    Crea una lista por comprensión con las cartas de la baraja española

    Pre:
        la función no recibe parámetros
    Post:
        naipes (list): la lista cargada con los valores y sus respectivos palos
    '''

    palos = ["Oro", "Copa", "Espada", "Basto"]
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

    naipes = []

    for palo in palos:
        for valor in valores:
            if valor == 10:
                nombre = "Sota"
            elif valor == 11:
                nombre = "Caballo"
            elif valor == 12:
                nombre = "Rey"
            else:
                nombre = str(valor)
            naipe = f"{nombre} de {palo}"
            naipes.append(naipe)
    return naipes

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa
    '''
    
    print(crear_lista())

main()