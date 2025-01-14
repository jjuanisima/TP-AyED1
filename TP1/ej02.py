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
        dia, mes, anio (int): fecha a validar
    Post:
        devuelve True si la fecha es válida, en caso contrario False
    '''
    if mes < 1 or mes > 12 or dia < 1 or anio < 1:
        return False
    
    if mes == 2:
        return dia <= 29 if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) else dia <= 28
        
    return dia <= 30 if mes in (4, 6, 9, 11) else dia <= 31
    
def main() -> None:
    '''
    Función principal que maneja el flujo del programa
    No recibe parámetros ni devuelve ningún valor
    '''
    try:
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))
    except ValueError:
        print("ERROR. Ingresa números enteros válidos :|\n")
        
    if fecha_valida(dia, mes, anio):
        print(f"La fecha {dia}/{mes}/{anio} es válida :)\n")
    else:
        print(f"La fecha {dia}/{mes}/{anio} es inválida :(\n")

if __name__ == "__main__":
    main()