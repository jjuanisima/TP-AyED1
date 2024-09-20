'''
Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la 
misma tiene 80 columnas.
'''


def centrar_cadena(cadena) -> None:
    '''
    Calcula el medio de la pantalla, restando lo que ocupa la cadena y dividiendo el resto por dos

    Pre:
        cadena (str): la cadena ingresada por el usuario
    Post:
        Printea la cadena en el medio de los 80 espacios
    '''

    espacios = (80 - len(cadena)) // 2
    print("|" + " " * espacios + cadena + " " * espacios + "|")

def main() -> None:
    '''
    Función principal, donde el usuario ingresa una cadena y se ejecuta el programa
    '''
    
    cadena = input("Ingrese una cadena: ")
    centrar_cadena(cadena)
    return None

main()