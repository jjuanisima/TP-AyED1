'''
La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del 
módulo math. Escribir un programa que utilice esta función para calcular la raíz 
cuadrada de un número cualquiera ingresado a través del teclado. El programa 
debe utilizar manejo de excepciones para evitar errores si se ingresa un número 
negativo.
'''


from math import sqrt

def calcular_raiz(num: float) -> str:
    '''
    Calcula la raíz cuadrada de un número positivo

    Pre:
        num (float): el número del cual se calcula la raíz cuadrada
    Post:
        un string con el resultado, o un mensaje de error si el número es inválido
    '''

    try:
        assert num >= 0, "ERROR. El número ingresado debe ser positivo :|"
        return f"La raíz de {num} es {sqrt(num)} :)"
    except AssertionError as m:
        return m

def main() -> None:
    '''
    Función principal, donde el usuario ingresa el número al cual calcular su raíz
    
    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    try:
        num = float(input("Número: "))
        print(calcular_raiz(num))
    except ValueError:
        print("ERROR. Revisa de ingresar un número :|")

main()