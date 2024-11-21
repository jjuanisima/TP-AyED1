'''
Realizar una función que devuelva el resto de dos números enteros, utilizando res
tas sucesivas
'''

def resta_sucesiva(a: int, b: int) -> int:
    '''
    Calcula el resto de dos números mediante restas

    Pre:
        a, b (int): el dividendo y el divisor
    Post:
        devuelve el resto
    '''

    if a < b:
        return a
    else:
        return resta_sucesiva(a - b, b)

if __name__ == "__main__":
    try:
        a = int(input("Dividendo: "))
        b = int(input("Divisor: "))
    except ValueError:
        print("ERROR. Intenta con números enteros :|")
    else:
        resultado = resta_sucesiva(a, b)
        print(f"{a} / {b} = {a//b}, resto {resultado}")
