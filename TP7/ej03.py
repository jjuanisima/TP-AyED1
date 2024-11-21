'''
Escribir una función que devuelva la suma de los N primeros números naturales.
'''

def sumar_naturales(num: int) -> int:
    '''
    Suma los primeros N números naturales, siendo N ingresado por el usuario

    Pre:
        num (int): el número N
    Post:
        devuelve la suma
    '''
    if num == 0:
        return 0
    else:
        return num + sumar_naturales(num - 1)
    
if __name__ == "__main__":
    try:
        num = int(input("Número: "))
    except ValueError:
        print("ERROR. Intenta con un número entero :|")
    else:
        numeros = " + ".join(str(i) for i in range(1, num + 1))
        resultado = sumar_naturales(num)
        print(f"{numeros} = {resultado}")
