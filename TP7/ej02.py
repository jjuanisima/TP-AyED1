'''
Desarrollar una función que reciba un número binario y lo devuelva convertido a 
base decimal. 
'''

def binario_a_decimal(binario: int, posicion: int) -> int:
    '''
    Convierte un número binario a decimal

    Pre:
        binario (int): el número binario a procesar
    Post:
        devuelve el número binario convertido a decimal
    '''

    if binario == 0:
        return 0
    else:
        return binario % 10 * (2 ** posicion) + binario_a_decimal(binario // 10, posicion + 1)                  
    
if __name__ == "__main__":
    try:
        binario = int(input("Binario: "))
    except ValueError:
        print("ERROR. Intenta con un número entero :|")
    else:
        posicion = 0
        print(binario_a_decimal(binario, posicion))