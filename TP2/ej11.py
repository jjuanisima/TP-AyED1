'''
Resolver el siguiente problema, diseñando las funciones a utilizar:
    Una clínica necesita un programa para atender a sus pacientes. Cada paciente que 
ingresa se anuncia en la recepción indicando su número de afiliado (número entero 
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con 
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego 
se solicita:
    a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de 
los pacientes atendidos por turno en el orden que llegaron a la clínica.
    b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue 
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta 
que se ingrese -1 como número de afiliado. 
'''


def validar_afiliado(num_afiliado: int) -> bool:
    '''
    Valida si el número de afiliado es un número entero de cuatro dígitos

    Pre:
        num_afiliado (int): el número a validar
    Post:
        true: el número es válido
        false: el número es inválido
    '''

    return num_afiliado >= 1000 and num_afiliado <= 9999

def validar_urgencia_o_turno(urgencia_o_turno: int) -> bool:
    '''
    Valida si el usuario ingresa urgencia o turno

    Pre:
        urgencia_o_turno (int): 0 es urgencia, 1 es turno
    Post:
        true: el número ingresado es válido
        false: el número ingresado es inválido
    '''

    return urgencia_o_turno == 0 or urgencia_o_turno == 1

def pacientes_urgencia_y_turno(num_afiliado: int, urgencia_o_turno: int) -> tuple:
    '''
    Se crean listados para los pacientes atendidos por urgencia y los atendidos por turno

    Pre:
        num_afiliado (int): el número de afiliado
        urgencia_o_turno (int): urgencia (0) o turno (1)
    Post:
        urgencia, turno (tuple): listados de pacientes
    '''

    if urgencia_o_turno == 0:
        urgencia.append(num_afiliado)
    else:
        turno.append(num_afiliado)
    return urgencia, turno

def buscar_afiliado(num_afiliado: int) -> str:
    '''
    Se busca un paciente y se informa cuántas veces se atendió por urgencia y cuántas veces por turno

    Pre:
        num_afiliado (int): número de afiliado del paciente
    Post:
        str: veces que fue atendido por turno, veces que fue atendido por urgencia
    '''

    cant_turnos = 0
    cant_urgencias = 0
    for num in turno:
        if num_afiliado in turno:
            cant_turnos += 1

    for num in urgencia:
        if num_afiliado in urgencia:
            cant_urgencias += 1
    return f"Atendido por turno: {cant_turnos} veces. Atendido por urgencia: {cant_urgencias} veces."

def main() -> None:
    '''
    Función principal, donde el usuario ingresa el número de afiliado del paciente y si fue atendido por urgencia o por turno
    '''
    
    num_afiliado = 0
    while num_afiliado != -1:
        try:
            num_afiliado = int(input("Número de afiliado: "))
            if validar_afiliado(num_afiliado):
                urgencia_o_turno = int(input("Urgencia o con turno: "))
                if validar_urgencia_o_turno(urgencia_o_turno):
                    pacientes_urgencia_y_turno(num_afiliado, urgencia_o_turno)
                    print(buscar_afiliado(num_afiliado))
                else:
                    print("ERROR. Revisa que urgencia o turno corresponda a 0 o 1.")
            else:
                print("ERROR. Revisa que el número de afiliado tenga 4 dígitos.")
        except ValueError:
            print("ERROR. Revisa de ingresar números enteros.")
    return None

afiliados = []
urgencia = []
turno = []

main()