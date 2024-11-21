'''
La siguiente función permite averiguar el día de la semana para una fecha determi
nada. La fecha se suministra en forma de tres parámetros enteros y la función de
vuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para 
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes 
y año cualquiera basándose en la función suministrada. Considerar que la semana 
comienza en domingo.
'''


from tabulate import tabulate

def diadelasemana(dia: int, mes: int, año: int) -> int:
    '''
    Calcula el día de la semana para una fecha

    Pre:
        dia, mes, año (int): la fecha
    Post:
        devuelve el día, donde 0 es domingo, 1 es lunes, y así sucesivamente
    '''

    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26 * mes - 2) // 10) + dia + año2 + (año2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def dias_por_mes(mes: int, año: int) -> int:
    '''
    Calcula la cantidad de días en un mes dado
    
    Pre:
        mes, año (int): el mes y el año (se considera si el año es bisiesto)
    Post:
        devuelve el número de días en el mes
    '''

    if mes in (4, 6, 9, 11):
        return 30
    elif mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 31

def nombres_mes(mes: int) -> str:
    '''
    Devuelve el nombre del mes correspondiente al número de mes dado

    Pre:
        mes (int): el número de mes (1 a 12)
    Post:
        devuelve el nombre del mes
    '''

    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    if mes in meses.keys():
        return meses[mes]

def printear_calendario(mes: int, año: int, nombre_mes: str) -> None:
    '''
    Imprime el calendario de un mes y año dados

    Pre:
        mes, año (int): el mes y el año a printear en el calendario
        nombre_mes (str): el nombre correspondiente al mes
    Post:
        no devuelve nada, sólo printea
    '''

    dia_uno = diadelasemana(1, mes, año)
    dias_mes = dias_por_mes(mes, año)

    dias_semana = ("Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb")

    calendario = []
    semana = ["   "] * dia_uno

    for dia in range(1, dias_mes + 1):
        semana.append(dia)
        if len(semana) == 7:
            calendario.append(semana)
            semana = []

    if semana:
        calendario.append(semana)

    print(f"Calendario {nombre_mes} {año}\n")
    print(tabulate(calendario, headers=dias_semana, tablefmt="keys", stralign="right"))

if __name__ == "__main__":
    mes = int(input("Mes: "))
    año = int(input("Año: "))
    nombre_mes = nombres_mes(mes)
    printear_calendario(mes, año, nombre_mes)