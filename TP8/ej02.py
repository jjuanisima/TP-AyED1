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
    anio += 1900 if anio > anio_corte else 2000

    return f"{dia} de {meses[mes - 1]} de {anio}"

def validar_fecha(partes: list[str]) -> tuple[int, int, int]:
    '''
    Valida las partes de una fecha y la convierte a formato entero

    Pre:
        partes (list[str]): lista con día, mes y año como cadenas
    Post:
        devuelve una tupla (dia, mes, año) si la fecha es válida. En caso contrario levanta un ValueError
    '''
    
    if len(partes) != 3:
        raise ValueError("Revisa que la fecha tenga formato DD/MM/AA :|")

    dia, mes, anio = map(int, partes)
    if not (dia >= 1 and dia <= 31):
        raise ValueError("El día tiene que estar entre 1 y 31 :|")
    if not (mes >= 1 and mes <= 12):
        raise ValueError("El mes debe estar entre 1 y 12 :|")
    if not len(str(anio)) == 2:
        raise ValueError("El año debe tener sólo dos dígitos :|")
    
    return dia, mes, anio

if __name__ == "__main__":
    try:
        fecha_str = input("Ingrese la fecha DD/MM/AA: ").strip()
        partes = fecha_str.split("/")
        
        fecha = validar_fecha(partes)

        print(fecha_extendida(fecha))
    except ValueError as e:
        print(f"ERROR: {e}")