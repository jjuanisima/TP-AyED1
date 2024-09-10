'''
Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una 
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros 
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones 
ni agregados, desarrollar programas que permitan:
    a. Sumar N días a una fecha.
    b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
'''


def dias_por_mes(mes: int, año: int) -> int:
    '''
    Devuelve el número máximo de días de un mes

    Pre:
        mes (int): el mes del año (1 a 12)
        año (int): el año para verificar si es bisiesto
    Post:
        int: el número máximo de días en el mes
    '''

    if mes in (4, 6, 9, 11):
        return 30
    
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    
    if mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            return 29
        return 28

def diasiguiente(dia: int, mes: int, año: int) -> str:
    '''
    Calcula el día siguiente a una fecha dada

    Pre:
        dia (int): el día del mes
        mes (int): el mes del año
        año (int): el año
    Post:
        str: la fecha del día siguiente
    '''

    dias = dias_por_mes(mes, año)
    dia += 1
    if dia > dias:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            año += 1

    return f"La fecha siguiente es {dia}/{mes}/{año}"

def main() -> None:
    '''
    Función principal, donde el usuario ingresa la fecha inicial
    '''

    try:
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        año = int(input("Año: "))
        print(diasiguiente(dia, mes, año))
    except ValueError:
        print("ERROR. Revisa que los valores de día, mes y año sean números enteros.")
    return None

main()