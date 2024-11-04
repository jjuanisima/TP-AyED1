'''
Desarrollar una función que devuelva una cadena de caracteres con el nombre del 
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán 
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función. 
Devolver una cadena vacía si el número de mes es inválido. La detección de meses 
inválidos deberá realizarse a través de excepciones.
'''


def devolver_mes(num_mes: int) -> str:
    '''
    Recibe un número de mes y devuelve el nombre del mes

    Pre:
        num_mes (int): número de mes a buscar en la lista
    Post:
        si el mes es válido devuelve su nombre, en caso contrario devuelve una cadena vacía
    '''

    meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre"
    ]

    try:
        return meses[num_mes - 1]
    except IndexError:
        return ""

def main() -> None:
    '''
    Función principal, donde se le solicita al usuario un número de mes a mostrar

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    try:
        num_mes = int(input("Número de mes: "))
        resultado = devolver_mes(num_mes)
        if resultado:
            print(f"El mes {num_mes} es {resultado} :)")
        else:
            print("ERROR. El número de mes ingresado no pertenece a ningún mes :|")
    except ValueError:
        print("ERROR. Revisa que el mes ingresado sea un número entero :|")

main()