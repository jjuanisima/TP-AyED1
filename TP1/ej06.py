'''
Desarrollar una función que reciba como parámetros dos números enteros positivos 
y devuelva como valor de retorno el número que resulte de concatenar ambos 
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se per
mite utilizar facilidades de Python no vistas en clase.
'''


def concatenar_numeros(a: int, b: int) -> int:
    '''
    Multiplica al número "a" por 10 elevado a la cantidad de dígitos que tenga "b", para que después sea posible sumarle "b" y que se concatenen los números

    Pre:
        a (int): número A
        b (int): número B
    Post:
        numero_final (int): la concatenación de "a" y "b"
    '''

    numero_final = a * (10 ** len(str(b))) + b
    return f"Número concatenado: {numero_final}"

def main() -> None:
    '''
    Función principal, donde el usuario ingresa los dos números a concatenar
    '''

    try:
        a = int(input("Número A: "))
        b = int(input("Número B: "))
        print(concatenar_numeros(a, b))
    except ValueError:
        print("ERROR. Revisa que ambos números sean enteros.")
    return None

main()