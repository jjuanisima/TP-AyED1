'''
Desarrollar una función que reciba tres números enteros positivos y devuelva el 
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en 
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar 
también un programa para ingresar los tres valores, invocar a la función y mostrar 
el máximo hallado, o un mensaje informativo si éste no existe.
'''


def mayor_estricto(a: int, b: int, c: int) -> int:
    '''
    Busca al mayor estricto entre los tres números.

    Pre:
        a (int): número A
        b (int): número B
        c (int): número C
    Post:
        int a, b ó c: el que resulte ser el mayor estricto entre los tres
        int -1: los tres números son iguales, o sea que no hay un mayor estricto
    '''

    mayor = -1

    if a > b:
        if a > c:
            if a != b:
                if a != c:
                    mayor = a
    if b > a:
        if b > c:
            if b != a:
                if b != c:
                    mayor = b
    if c > a:
        if c > b:
            if c != a:
                if c != b:
                    mayor = c
    return mayor

def main() -> None:
    '''
    Función principal, donde el usuario ingresa los tres números solicitados
    '''

    try:
        a = int(input("Número A: "))
        b = int(input("Número B: "))
        c = int(input("Número C: "))

        if a < 1 or b < 1 or c < 1:
            print("ERROR. Intenta con números positivos.")

        if mayor_estricto(a, b, c) == -1:
            print("Los tres números ingresados son iguales :|")
        else:
            print(f"El mayor estricto es el número {mayor_estricto(a, b, c)}")
    except ValueError:
        print("ERROR. Intenta ingresando números enteros.")
    return None

main()