'''
Resolver el siguiente problema, utilizando funciones:
    Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se 
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de car
ga. Se solicita:
    a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe 
aparecer una sola vez en el informe.
    b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus 
ingresos. Mostrar los registros de entrada al club antes y después de 
eliminarlo. Informar cuántos ingresos se eliminaron.
'''


def menu_opciones() -> None:
    '''
    Printea las opciones del menú
    '''
    print("\nREGISTRO DE SOCIOS.")
    print("1. Registrar un ingreso.")
    print("2. Informar cuántas veces ingresó un socio.")
    print("3. Dar de baja un socio.")

def validar_num_socio(num_socio: int) -> bool:
    '''
    Valida si el número de socio tiene cinco dígitos
    
    Pre:
        num_socio (int): el número de socio a validar
    Post:
        true: el número de socio es válido
        false: el número de socio es inválido
    '''

    return num_socio >= 10000 and num_socio <= 99999

def registrar_ingresos(num_socio, ingresos) -> None:
    '''
    Se registra el número de socio y cuántas veces ingresó al club

    Pre:
        num_socio (int): el número de socio
    Post:
        Modifica el diccionario de ingresos
    '''

    if num_socio in ingresos:
        ingresos[num_socio] += 1
    else:
        ingresos[num_socio] = 1
    return None

def mostrar_ingresos(ingresos) -> None:
    '''
    Printea los ingresos por socio en el día

    Pre:
        ingresos (dict): los ingresos registrados en el día
    Post:
        Se printea el número de socio y cuántas veces ingresó al club
    '''

    print("\nIngresos por socio:")
    for socio, cantidad in ingresos.items():
        print(f"Socio {socio}: {cantidad} ingresos.")

def baja_del_club(socio_baja, ingresos) -> None:
    '''
    Busca el número de socio y lo elimina de los ingresos

    Pre:
        socio_baja (int): el número de socio
        ingresos (dict): los ingresos registrados en el día
    Post:
        Modifica el diccionario de ingresos
    '''

    if socio_baja in ingresos:
        cant_bajas = ingresos.pop(socio_baja)
        print(f"\nSe eliminaron {cant_bajas} ingresos del socio {socio_baja}.")

    print("\nRegistros de entrada después de eliminar a un socio:")
    mostrar_ingresos(ingresos)

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa con un menú
    '''

    ingresos = {}
    while True:
        menu_opciones()
        op = input("\nElegí una opción: ")
        if op == '1':
            num_socio = -1
            while num_socio != 0:
                num_socio = int(input("Número de socio: "))
                if num_socio == 0:
                    break
                if validar_num_socio(num_socio):
                    registrar_ingresos(num_socio, ingresos)
                else:
                    print("ERROR. Número de socio inválido.")
        elif op == '2':
            mostrar_ingresos(ingresos)
        elif op == '3':
            socio_baja = int(input("Dar socio de baja: "))
            baja_del_club(socio_baja, ingresos)
        else:
            print("ERROR. Opción inválida")
    return None

main()