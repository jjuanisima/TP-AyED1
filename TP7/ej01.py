'''
Escribir una función que devuelva la cantidad de dígitos de un número entero, sin 
utilizar cadenas de caracteres.
'''

def cant_digitos(num: int) -> int:
    '''
    Calcula la cantidad de dígitos de un número

    Pre:
        num (int): el número inicial
    Post:
        devuelve la cantidad de dígitos del número
    '''
    
    if num < 10:
        return 1
    else:
        return 1 + cant_digitos(num // 10)
    
if __name__ == "__main__":
    try:
        num = int(input("Número: "))
    except ValueError:
        print("ERROR. Intenta con un número entero :|")
    else:
        resultado = cant_digitos(num)
        print(f"Nro de dígitos: {resultado}")