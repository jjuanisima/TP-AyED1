'''
Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas 
en cada una de sus plantas durante una semana. De este modo, cada columna re
presenta el día de la semana y cada fila a una de sus fábricas. 
Se solicita:
    a. Crear una matriz con datos generados al azar para N fábricas durante una 
semana, considerando que la capacidad máxima de fabricación es de 150 
unidades por día y puede suceder que en ciertos días no se fabrique nin
guna. 
    b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica. 
    c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
    d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
    e. Crear una lista por comprensión que contenga la menor cantidad fabricada 
por cada fábrica.
'''


import random as rn

def crear_matriz(n: int) -> list:
    '''
    Crea una matriz tipo semanal para N fábricas, con valores de fabricación entre 0 y 150

    Pre:
        n (int): valor de n, que define la cantidad de fábricas
    Post:
        matriz (list): la matriz semanal con los números cargados
    '''

    matriz = []
    for i in range(n):
        fila = []
        for j in range(7):
            fila.append(rn.randint(0, 150))
        matriz.append(fila)
    return matriz

def bicicletas_por_fabrica(matriz) -> None:
    '''
    Muestra la cantidad de bicicletas fabricadas por cada fábrica

    Pre:
        matriz (list): la matriz de producción semanal
    Post:
        Printea cada matriz con su respectiva producción
    '''

    for i in range(len(matriz)):
        total = 0
        for j in range(len(matriz[i])):
            total += matriz[i][j]
        print(f"Fábrica {i+1}: {total} bicicletas.")

def fabrica_mayor_produccion(matriz) -> str:
    '''
    Muestra la fábrica que más produjo en un día específico

    Pre:
        matriz (list): la matriz de producción semanal
    Post:
        Retorna el número de fábrica y el día
    '''

    max_produccion = 0
    fabrica_max = 0
    dia_max = 0
    for i in range(len(matriz)):
        for j in range(7):
            if matriz[i][j] > max_produccion:
                max_produccion = matriz[i][j]
                fabrica_max = i
                dia_max = j
    return f"\nFábrica que más produjo en un día: {fabrica_max + 1}. Día: {dia_max + 1}."

def dia_mas_productivo(matriz) -> str:
    '''
    Busca el día más productivo, teniendo en cuenta la producción de todas las fábricas

    Pre:
        matriz (lista): la matriz de producción semanal
    Post:
        Retorna el día más productivo
    '''
    
    suma_por_dia = [0, 0, 0, 0, 0, 0, 0]

    for i in range(len(matriz)):
        for j in range(7):
            suma_por_dia[j] += matriz[i][j]

    dia_max = 0
    for i in range(7):
        if suma_por_dia[i] > suma_por_dia[dia_max]:
            dia_max = i

    return f"\nDía más productivo: {dia_max + 1}"

def menor_produccion_por_fabricante(matriz) -> list:
    '''
    Busca la menor cantidad fabricada por cada fábrica

    Pre:
        matriz (list): la matriz de producción semanal
    Post:
        menor (list): una lista con la menor producción de cada fábrica
    '''

    menor = [min(fila) for fila in matriz]
    return menor

def main() -> None:
    '''
    Función principal, donde el usuario ingresa el valor de N y se ejecuta el programa
    '''

    n = int(input("Valor de N (cantidad de fábricas): "))
    matriz = crear_matriz(n)

    print("Matriz de producción semanal:")
    for fila in matriz:
        print(fila)

    print("\nCantidad total de bicicletas fabricadas por cada fábrica:")
    bicicletas_por_fabrica(matriz)

    print(fabrica_mayor_produccion(matriz))

    print(dia_mas_productivo(matriz))

    menor_produccion = menor_produccion_por_fabricante(matriz)
    print("\nMenor cantidad fabricada por cada fábrica:")
    for i in range(len(menor_produccion)):
        print(f"Fábrica {i+1}: {menor_produccion[i]} bicicletas.")

main()