'''
Desarrollar una función que devuelva el producto de dos números enteros por su
mas sucesivas
'''

def producto_sucesivo(a: int, b: int) -> int:
    '''
    Suma al número 'a' por sí mismo una 'b' cantidad de veces, o sea una suma sucesiva

    Pre:
        a, b (int): los números a calcular su producto
    Post:
        devuelve el producto de 'a' y 'b'
    '''

    if b == 0:
        return 0
    else:
        return a + (producto_sucesivo(a, b - 1))

if __name__ == "__main__":
    try:
        a = int(input("Número A: "))
        b = int(input("Número B: "))
    except ValueError:
        print("ERROR. Intenta con números enteros :|")
    else:
        numeros = " + ".join(str(a) for _ in range(b))
        resultado = producto_sucesivo(a, b)
        print(f"{numeros}: {resultado}")
