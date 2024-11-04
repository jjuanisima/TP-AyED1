'''
Desarrollar una función para ingresar a través del teclado un número natural. La 
función rechazará cualquier ingreso inválido de datos utilizando excepciones y 
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese 
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón 
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea 
correcto. Escribir también un programa que permita probar el correcto funciona
miento de la misma.
'''


def validar_numero(num_input: str) -> int:
    '''
    Valida que el número de entrada sea un número natural

    Pre:
        num_input (str): el input del usuario, que se va a convertir a número
    Post:
        retorna el número entero si es válido, de lo contrario retorna None
    '''

    try:
        num = float(num_input)

        if num.is_integer():
            num = int(num)
            assert num > 0, "ERROR. El número debe ser mayor que 0 :|"
        else:
            raise ValueError("ERROR. El número debe ser entero, no flotante :|")

    except (AssertionError, ValueError) as m:
        print(m)
        return -1
    
    return num
        
def main() -> None:
    '''
    Función principal, donde se le solicita al usuario un número natural y se valida su entrada
    
    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    try:
        num_input = input("Ingrese un número natural: ")
        resultado = validar_numero(num_input)
        if resultado is not -1:
            print(f"{resultado} es un número válido :)")
    except ValueError:
        print("ERROR. Revisa de ingresar un número natural :|")

main()