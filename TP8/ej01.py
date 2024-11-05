'''
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho
rarios, y luego escribir un programa que las vincule:
    a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha 
válida.
    b. Sumar N días a una fecha.
    c. Ingresar un horario desde teclado, verificando que sea correcto.
    d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al 
segundo se considerará que el primero corresponde al día anterior. En ningún 
caso la diferencia en horas puede superar las 24 horas.
'''


def menu_opciones() -> None:
    '''
    Muestra las opciones del menú disponibles para el usuario

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    print("\nMENÚ:")
    print("1. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha válida.")
    print("2. Sumar N días a una fecha.")
    print("3. Ingresar un horario desde teclado, verificando que sea correcto.")
    print("4. Calcular la diferencia entre dos horarios.")

# Opción A
def fecha_valida(fecha: tuple[int, int, int]) -> bool:
    '''
    Verifica si la fecha ingresada es válida

    Pre:
        fecha (tuple[int, int, int]): una tupla que contiene el día, mes y año
    Post:
        retorna True si la fecha es válida, False en caso contrario
    '''

    dia, mes, anio = fecha
    if dia < 1 or dia > 31:
        return False
    if mes < 1 or mes > 12:
        return False
    if mes in (1, 3, 5, 7, 8, 10, 12) and dia > 31:
        return False
    if mes in (4, 6, 9, 11) and dia > 30:
        return False
    if mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) and dia > 29:
            return False
        else:
            if dia > 28:
                return False
    return True

# Opción B
def dias_por_mes(mes: int, anio: int) -> int:
    '''
    Devuelve la cantidad de días en un mes determinado del año

    Pre:
        mes (int): el mes (1-12)
        anio (int): el año
    Post:
        retorna el número de días en el mes
    '''

    if mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return 29
        else:
            return 28
    elif mes in (4, 6, 9, 11):
        return 30
    return 31

def sumar_dias(fecha: tuple[int, int, int], dias_a_sumar: int) -> tuple[int, int, int]:
    '''
    Suma un número de días a una fecha dada.

    Pre:
        fecha (tuple[int, int, int]): una tupla con el día, mes y año
        dias_a_sumar (int): la cantidad de días a sumar
    Post:
        retorna una nueva tupla con la fecha resultante (dia, mes, año)
    '''

    dia, mes, anio = fecha
    if dia + dias_a_sumar <= dias_por_mes(mes, anio):
        dia += dias_a_sumar
    else:
        dias_a_sumar -= (dias_por_mes(mes, anio) - dia)
        dia = 1 + (dias_a_sumar - 1)
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1
    return dia, mes, anio

# Opción C
def validar_horario(hora_completa: tuple[int, int]) -> bool:
    '''
    Valida si el horario es correcto

    Pre:
        hora_completa: una tupla con la hora y los minutos
    Post:
        retorna True si el horario es válido, False en caso contrario
    '''

    hora, minutos = hora_completa
    return hora >= 0 and hora <= 23 and minutos >= 0 and minutos <= 59

# Opción D
def diferencia_horarios(horario1: tuple[int, int], horario2: tuple[int, int]) -> tuple[int, int]:
    '''
    Calcula la diferencia entre dos horarios

    Pre:
        horario1 (tuple[int, int]): primer horario como tupla (hora, minutos)
        horario2 (tuple[int, int]): segundo horario como tupla (hora, minutos)
    Post:
        retorna la diferencia en horas y minutos como una tupla (horas, minutos)
    '''

    h1, m1 = horario1
    h2, m2 = horario2

    if h2 > h1:
        horas = h2 - h1
        if m2 > m1:
            minutos = m2 - m1
        else:
            horas -= 1
            minutos = (m2 + 60) - m1
    else:
        horas = (h2 + 24) - h1
        if m2 > m1:
            minutos = m2 - m1
        else:
            horas -= 1
            minutos = (m2 + 60) - m1
    return horas, minutos

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    op = -1
    while op != 0:
        menu_opciones()
        try:
            op = int(input("\nSeleccione una opción: "))
            match op:
                case 1:
                    dia = int(input("Día: "))
                    mes = int(input("Mes: "))
                    anio = int(input("Año: "))
                    fecha = (dia, mes, anio)
                    if fecha_valida(fecha):
                        print(f"'{dia}/{mes}/{anio}' es una fecha válida :)")
                    else:
                        print(f"'{dia}/{mes}/{anio}' es una fecha inválida :(")
                case 2:
                    dia = int(input("Día: "))
                    mes = int(input("Mes: "))
                    anio = int(input("Año: "))
                    dias_a_sumar = int(input("Días a sumar: "))
                    fecha = (dia, mes, anio)
                    print(sumar_dias(fecha, dias_a_sumar))
                case 3:
                    hora = int(input("Hora (0-23): "))
                    minutos = int(input("Minutos (0-59): "))
                    hora_completa = (hora, minutos)
                    if validar_horario(hora_completa):
                        print(f"'{hora}:{minutos}' es una hora válida :)")
                    else:
                        print(f"'{hora}:{minutos}' es una hora inválida :(")
                case 4:
                    h1 = int(input("Hora 1 (0-23): "))
                    m1 = int(input("Minutos 1 (0-59): "))
                    h2 = int(input("Hora 2 (0-23): "))
                    m2 = int(input("Minutos 2 (0-59): "))
                    horario1 = (h1, m1)
                    horario2 = (h2, m2)
                    hora, minutos = diferencia_horarios(horario1, horario2)
                    print(f"Hay una diferencia de {hora}:{minutos}")
                case 5:
                    print("Saliendo...")
                case _:
                    print("Opción inválida :|")
        except ValueError:
            print("ERROR. Revisa de ingresar un número :|")

main()