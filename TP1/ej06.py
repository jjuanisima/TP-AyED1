'''
Desarrollar una función que reciba como parámetros dos números enteros positivos 
y devuelva como valor de retorno el número que resulte de concatenar ambos 
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se per
mite utilizar facilidades de Python no vistas en clase.
'''


def concatenar_numeros(a: int, b: int) -> int:
    '''
    Se le agrega a 'a' una cant. de ceros equivalente a la cant. de dígitos de 'b' para que sea posible la concatenación
    Pre:
        a, b (int): números a concatenar
    Post:
        devuelve el número final
    '''

    numero_final = a * (10 ** len(str(b))) + b
    return numero_final

if __name__ == "__main__":
    try:
        a = int(input("Número A: "))
        b = int(input("Número B: "))

        resultado = concatenar_numeros(a, b)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("ERROR. Revisa que ambos números sean enteros.")