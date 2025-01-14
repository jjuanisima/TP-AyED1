'''
Desarrollar una función que reciba como parámetros dos números enteros positivos 
y devuelva como valor de retorno el número que resulte de concatenar ambos 
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se per
mite utilizar facilidades de Python no vistas en clase.
'''


def main() -> None:
    '''
    Función principal que maneja el flujo del programa
    No recibe parámetros ni devuelve ningún valor
    '''
    # Se le agrega a 'a' una cant. de ceros equivalente a la cant. de dígitos de 'b' para que sea posible la concatenación
    concatenar = lambda x, y: x * (10 ** len(str(y))) + y

    try:
        a = int(input("Número A: "))
        b = int(input("Número B: "))
    except ValueError:
        print("ERROR. Revisa que ambos números sean enteros.")
    
    resultado = concatenar(a, b)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()