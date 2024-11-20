'''
Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una 
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros 
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones 
ni agregados, desarrollar programas que permitan:
    a. Sumar N días a una fecha.
    b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
'''


def menu_opciones() -> None:
    '''
    Muestra las opciones del menú
    Pre:
        no recibe parámetros
    Post:
        devuelve un diccionario con el número de opción como clave y la descripción como valor
    '''

    opciones = {
        1: "Calcular el día siguiente a una fecha",
        2: "Sumar N días a una fecha",
        3: "Calcular la cantidad de días entre dos fechas",
        0: "Salir del programa"
    }
    return opciones

def dias_por_mes(mes: int, anio: int) -> int:
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
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return 29
        return 28

def diasiguiente(dia: int, mes: int, anio: int) -> tuple:
    '''
    Calcula el día siguiente a una fecha dada

    Pre:
        dia, mes, anio (int): la fecha
    Post:
        devuelve una tupla con la fecha del día siguiente a la fecha dada
    '''

    dias = dias_por_mes(mes, anio)
    dia += 1
    if dia > dias:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1
    return dia, mes, anio

def sumar_dias(dia: int, mes: int, anio: int, dias: int) -> tuple:
    '''
    Suma N cantidad de días a la fecha inicial
    Pre:
        dia, mes, anio (int): la fecha
        dias (int): cantidad de días a sumar
    Post:
        devuelve una tupla con la fecha final
    '''

    for _ in range(dias):
        dia, mes, anio = diasiguiente(dia, mes, anio)
    return dia, mes, anio

def dias_entre_fechas(fecha1: tuple, fecha2: tuple) -> int:
    '''
    Calcula la cantidad de días entre dos fechas dadas

    Pre:
        fecha1, fecha2 (tuple): las fechas en formato (día, mes, año)
    Post:
        devuelve la cantidad de días entre las dos fechas
    '''

    dia1, mes1, anio1 = fecha1
    dia2, mes2, anio2 = fecha2

    cant_dias = 0
    while (dia1, mes1, anio1) != (dia2, mes2, anio2):
        dia1, mes1, anio1 = diasiguiente(dia1, mes1, anio1)
        cant_dias += 1
    return cant_dias

def ingresar_fecha() -> tuple:
    '''
    Pide al usuario que ingrese una fecha

    Pre:
        no recibe parámetros
    Post:
        devuelve una tupla con la fecha correspondiente
    '''
    
    while True:
        try:
            dia = int(input("Día: "))
            mes = int(input("Mes: "))
            anio = int(input("Año: "))
            if mes >= 1 and mes <= 12 and dia > 1 and dia <= dias_por_mes(mes, anio):
                return dia, mes, anio
            else:
                print("ERROR. La fecha ingresada no es válida :|\n")
        except ValueError:
            print("ERROR. Revisa que día, mes y año sean números enteros :|\n")

if __name__ == "__main__":
    while True:
        opciones = menu_opciones()
        for num, opcion in opciones.items():
            print(f"{num}. {opcion}")
        try:
            op = int(input("\nIngrese una opción: "))
            print()
            match op:
                case 1:
                    dia, mes, anio = ingresar_fecha()
                    dia_siguiente = diasiguiente(dia, mes, anio)
                    dia2, mes2, anio2 = dia_siguiente
                    print(f"El día siguiente a {dia}/{mes}/{anio} es {dia2}/{mes2}/{anio2} :)\n")
                case 2:
                    dia, mes, anio = ingresar_fecha()
                    dias = int(input("Días a sumar a la fecha dada: "))
                    dia_n, mes_n, anio_n = sumar_dias(dia, mes, anio, dias)
                    print(f"Fecha + {dias} días: {dia_n}/{mes_n}/{anio_n}\n")
                case 3:
                    print("Ingrese la primera fecha: ")
                    dia, mes, anio = ingresar_fecha()
                    print("\nIngrese la segunda fecha: ")
                    dia2, mes2, anio2 = ingresar_fecha()

                    fecha1 = (dia, mes, anio)
                    fecha2 = (dia2, mes2, anio2)
                    diferencia = dias_entre_fechas(fecha1, fecha2)
                    print(f"Hay {diferencia} días entre {dia}/{mes}/{anio} y {dia2}/{mes2}/{anio2}\n")
                case 0:
                    print("Saliendo...")
                    break
                case _:
                    print("ERROR. Elija una opción válida :|")
                    continue          
        except ValueError:
            print("ERROR. Ingrese un número válido para la opción :|")