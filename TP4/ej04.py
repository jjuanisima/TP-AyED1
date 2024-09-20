'''
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y 
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En 
qué cambiaría la función si el rango de valores fuese diferente?
'''


def validar_num(num) -> bool:
    '''
    Valida si el número está entre 0 y 3999

    Pre:
        num (int): el número a validar
    Post:
        true: el número es válido
        false: el número es inválido
    '''

    return num >= 0 and num <= 3999

def numero_romano(num) -> str:
    '''
    Convierte un número entero a su equivalente en números romanos

    Pre:
        num (int): el número ingresado por el usuario
    Post:
        str: la representación en números romanos del número entero
    '''

    valores_romanos = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    romano = ""
    for numero, letra in valores_romanos:
        while num >= numero:
            romano += letra
            num -= numero
    return romano

def main() -> None:
    '''
    Función principal, donde el usuario ingresa un número a validar y convertir a números romanos
    '''

    try:
        num = int(input("Ingrese un número (entre 0 y 3999): "))
        if validar_num(num):
            print(numero_romano(num))
        else:
            print("ERROR. Revisa que el número ingresado sea entre 0 y 3999.")
    except ValueError:
        print("ERROR. Revisa que el número ingresado sea un entero.")
    return None

main()