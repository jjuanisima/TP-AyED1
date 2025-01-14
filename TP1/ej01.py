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
        a, b, c (int): números enteros positivos
    Post:
        devuelve el mayor estricto, en caso contrario -1
    '''
    numeros = [a, b, c]
    mayor = max(numeros)
    if numeros.count(mayor) == 1:
        return mayor
    return -1

def main() -> None:
    '''
    Función principal que maneja el flujo del programa
    No recibe parámetros ni devuelve ningún valor
    '''
    try:
        a = int(input("Número A: "))
        b = int(input("Número B: "))
        c = int(input("Número C: "))
    except ValueError:
        print("ERROR. Intenta ingresando números enteros.")

    if a < 1 or b < 1 or c < 1:
        print("ERROR. Intenta con números positivos :|")
    else:
        resultado = mayor_estricto(a, b, c)
        if resultado == -1:
            print("Los tres números ingresados son iguales :|")
        else:
            print(f"El mayor estricto es el número {resultado} :)")

if __name__ == "__main__":
    main()