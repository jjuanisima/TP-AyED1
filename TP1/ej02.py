'''
Desarrollar una función que reciba tres números enteros positivos correspondientes 
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe 
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos. 
Devolver True o False según la fecha sea correcta o no. Realizar también un 
programa para verificar el comportamiento de la función.
'''


def fecha_valida(dia: int, mes: int, anio: int) -> bool:
    '''
    Verifica si la fecha ingresada es válida

    Pre:
        dia (int): día del mes
        mes (int): mes del año
        anio (int): el año
    Post:
        bool True: la fecha es válida
        bool False: la fecha es inválida
    '''

    if mes < 1 or mes > 12:
        return False
    if anio < 1:
        return False
    if mes in (4, 6, 9, 11):
        return dia >= 1 and dia <= 30
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return dia >= 1 and dia <= 31
    if mes == 2:
        if anio_bisiesto(anio):
            return dia <= 29
        return dia <= 28

def anio_bisiesto(anio: int) -> bool:
    '''
    Verifica si el año es bisiesto

    Pre:
        anio (int): el año a verificar
    Post:
        bool True: si es divisible por 400 o también es divisible por 4 pero no por 100, entonces el año es bisiesto
        bool False: si no se cumple la condición, el año no es bisiesto
    '''

    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def main() -> None:
    '''
    Función principal, donde el usuario ingresa la fecha a validar
    '''

    while True:
        try:
            dia = int(input("Día: "))
            mes = int(input("Mes: "))
            anio = int(input("Año: "))
            
            if fecha_valida(dia, mes, anio):
                print(f"La fecha {dia}/{mes}/{anio} es válida :)\n")
            else:
                print(f"La fecha {dia}/{mes}/{anio} es inválida :(\n")
        except ValueError:
            print("ERROR. Intenta de nuevo ingresando números enteros.\n")
    return None

main()