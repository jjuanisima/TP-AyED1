'''
Todo programa Python es susceptible de ser interrumpido mediante la pulsación de 
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar 
un programa para imprimir los números enteros entre 1 y 100000, y que solicite 
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
'''


def imprimir_numeros() -> None:
    '''
    Imprime los números del 1 al 100000, y en caso de interrumpirse el proceso le pregunta al usuario si desea continuar o detener el programa

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    try:
        for num in range(1, 100001):
            print(num)
    except KeyboardInterrupt:
        opcion = input("¿Desea detener el programa? ('S' para detener, 'N' para continuar): ")
        if opcion.upper() == 'S':
            print("Programa detenido :(")
        else:
            print("Continuemos... :)")
            imprimir_numeros()

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    imprimir_numeros()

main()