'''
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 
que no sean múltiplos de 5. A y B se ingresar desde el teclado. 
'''

def multiplos7(a, b):
    '''
    Crea una lista con los elementos de A y B que sean múltiplos de 7 pero no de 5

    Pre:
        a (int): número a, con el que inicia el rango
        b (int): número b, con el que termina el rango
    Post:
        list: lista con los números que cumplen la condición
    '''

    return [i for i in range(a, b) if i % 7 == 0 and i % 5 != 0]

def main() -> None:
    '''
    Función principal, donde el usuario ingresa los números A y B
    '''
    
    try:
        a = int(input("Número A: "))
        b = int(input("Número B: "))
        print(multiplos7(a, b))
    except ValueError:
        print("ERROR. Revisa que A y B sean números enteros.")
    return None

main()