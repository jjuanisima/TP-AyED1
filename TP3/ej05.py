'''
 Desarrollar un programa que permita realizar reservas en una sala de cine de N 
filas con M butacas por cada fila. Desarrollar las siguientes funciones y utilizarlas 
en un mismo programa:
    mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas 
del cine. Esta función deberá ser invocada antes de que se realice la reserva, y 
se volverá a invocar luego de la misma con los estados actualizados.
    reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la 
sala en caso de estar disponible dicha butaca. La función devolverá True/False 
si logró o no reservar la butaca.
    cargar_sala: Recibirá una matriz como parámetro y la cargará con valores 
aleatorios para simular una sala con butacas ya reservadas.
    butacas_libres: Recibirá como parámetro la matriz y retornará cuántas buta
cas desocupadas hay en la sala.
    butacas_contiguas: Buscará la secuencia más larga de butacas libres conti
guas en una misma fila y devolverá las coordenadas de inicio de la misma.
'''


import random as rn

def crear_sala(n: int, m: int) -> list:
    '''
    Crea una sala de cine de N * M, iniciando con todas las butacas libres

    Pre:
        n (int): cantidad de filas de la sala de cine
        m (int): cantidad de butacas de cada fila
    Post:
        sala (list): una matriz de N * M que representa la sala de cine
    '''

    return [["O"] * m for i in range(n)]

def mostrar_butacas(sala: list) -> None:
    '''
    Printea el estado actual de la sala de cine
    '''

    for fila in sala:
        print(fila)
    print()

def reservar(sala: list, fila: int, butaca: int) -> bool:
    '''
    Reserva una butaca en la sala de cine

    Pre:
        sala (list): la matriz que representa la sala de cine
        fila (int): fila donde se quiere realizar la reserva
        butaca (int): butaca que se quiere reservar
    Post:
        true: la reserva fue exitosa (o sea, la butaca estaba libre)
        false: la butaca ya estaba ocupada
    '''

    if sala[fila-1][butaca-1] == "O":
        sala[fila-1][butaca-1] = "X"
        return True
    return False

def cargar_sala(sala: list) -> None:
    '''
    Carga la sala con reservas random, simulando una sala parcialmente ocupada

    Pre:
        sala (list): la matriz que representa la sala de cine
    Post:
        la sala actualizada con reservas random
    '''

    for i in range(len(sala)):
        for j in range(len(sala[i])):
            sala[i][j] = rn.choice(["O", "X"])

def butacas_libres(sala: list) -> int:
    '''
    Cuenta cuántas butacas desocupadas hay en la sala

    Pre:
        sala (list): la matriz que representa la sala de cine
    Post:
        libres (int): la cantidad de butacas desocupadas que hay
    '''

    libres = 0
    for fila in sala:
        for butaca in fila:
            if butaca == "O":
                libres += 1
    return libres

def butacas_contiguas(sala: list) -> tuple:
    '''
    Busca la secuencia de butacas libres más larga

    Pre:
        sala (list): la matriz que representa la sala de cine
    Post:
        max_fila, max_inicio, max_longitud (tuple): la fila, la posición de inicio y la longitud de la secuencia más larga de butacas libres
    '''
    
    max_fila = 0
    max_inicio = 0
    max_longitud = 0

    for i in range(len(sala)):
        inicio = 0
        longitud = 0
        for j in range(len(sala[i])):
            if sala[i][j] == "O":
                if longitud == 0:
                    inicio = j
                longitud += 1
            else:
                if longitud > max_longitud:
                    max_longitud = longitud
                    max_fila = i
                    max_inicio = inicio
                longitud = 0

    if longitud > max_longitud:
        max_longitud = longitud
        max_fila = i
        max_inicio = inicio

    return max_fila, max_inicio, max_longitud
    
def main() -> None:
    '''
    Función principal, donde se ejecuta el programa
    '''

    n = 3
    m = 5
    sala = crear_sala(n, m)
    print("Estado actual de la sala:")
    mostrar_butacas(sala)
    print(f"Butacas libres: {butacas_libres(sala)}")

    cargar_sala(sala)
    print("\nEstado actual de la sala:")
    mostrar_butacas(sala)
    print(f"Butacas libres: {butacas_libres(sala)}")

    while True:
        fila = int(input("Fila: "))
        butaca = int(input("Butaca: "))

        if butacas_libres(sala) == 0:
            print("\nTodas las butacas están ocupadas. Sala llena :)")
            break

        if reservar(sala, fila, butaca):
            print("Reserva exitosa :)")
        else:
            print("ERROR. Butaca ya reservada :(")

        print("\nEstado actual de la sala:")
        mostrar_butacas(sala)
        print(f"Butacas libres: {butacas_libres(sala)}")

        fila, butaca, longitud = butacas_contiguas(sala)
        if longitud > 1:
            print(f"Secuencia más larga: Fila {fila+1}. Inicio: {butaca+1}. Longitud: {longitud}")
        else:
            print("ERROR. No hay secuencias de butacas libres seguidas.")

main()