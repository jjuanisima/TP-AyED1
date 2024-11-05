'''
Escribir una función que reciba como parámetro una tupla conteniendo una fecha 
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada 
en formato extendido. La función debe contemplarse que el año se ingrese en dos 
dígitos, los que serán interpretados según un año de corte definido dentro del 
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por 
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030" 
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de 
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en 
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y 
mostrar el resultado.
'''


def fecha_extendida(fecha: tuple[int, int, int]) -> str:
    '''
    Convierte una fecha representada como una tupla (día, mes, año) en una cadena con el mes representado en palabras

    Pre:
        fecha (tuple[int, int, int]): tupla que contiene el día, mes y año
    Post:
        una cadena que representa la fecha en formato extendido
    '''

    dia, mes, anio = fecha
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    anio_corte = 33
    if anio > anio_corte:
        anio += 1900
    else:
        anio += 2000

    return f"{dia} de {meses[mes - 1]} de {anio}"

def main() -> None:
    '''
    Función principal, donde se le solicita al usuario una fecha

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    try:
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))
        
        if len(str(anio)) > 2:
            print("ERROR. Revisa que el año tenga sólo 2 dígitos :|")
        else:
            fecha = (dia, mes, anio)

            print(fecha_extendida(fecha))
    except ValueError:
        print("ERROR. Revisa de ingresar valores numéricos :|")

main()