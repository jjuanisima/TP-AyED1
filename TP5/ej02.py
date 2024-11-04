'''
Realizar una función que reciba como parámetros dos cadenas de caracteres con
teniendo números reales, sume ambos valores y devuelva el resultado como un 
número real. Devolver -1 si alguna de las cadenas no contiene un número válido, 
utilizando manejo de excepciones para detectar el error.
'''


def sumar_valores(cadena1: str, cadena2: str) -> float:
    '''
    Castea los números de las cadenas de caracteres y los suma

    Pre:
        cadena1 (str): primera cadena que tiene que contener un número
        cadena1 (str): segunda cadena que tiene que contener un número
    Post:
        float: la suma de los números, o -1 si alguna cadena no es válida
    '''

    try:
        return float(cadena1) + float(cadena2)
    except ValueError:
        return -1

def main() -> None:
    '''
    Función principal, donde se solicita al usuario que ingrese dos cadenas a sumar

    Esta función no recibe parámetros y no devuelve ningún valor
    '''
    
    cadena1 = input("Primer número: ")
    cadena2 = input("Segundo número: ")
    resultado = sumar_valores(cadena1, cadena2)

    if resultado == -1:
        print("ERROR. Revisa de ingresar números reales :|")
    else:
        print(f"Resultado: {resultado}")

main()