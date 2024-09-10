'''
Una persona desea llevar el control de los gastos realizados al viajar en el subte
rráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un es
quema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarro
llar una función que reciba como parámetro la cantidad de viajes realizados en un 
determinado mes y devuelva el total gastado en viajes. Realizar también un pro
grama para verificar el comportamiento de la función.
'''


def calcular_gastos(viajes: int) -> float:
    '''
    Calcula el total gastado en viajes

    Pre:
        viajes (int): cantidad de viajes realizados en el mes
    Post:
        float: la tarifa con su respectivo descuento
    '''

    tarifa_maxima = 650
    total = 0.0

    if viajes > 40:
        total = viajes * (tarifa_maxima * 0.60)
    elif viajes >= 31 and viajes <= 40:
        total = viajes * (tarifa_maxima * 0.70)
    elif viajes >= 21 and viajes <= 30:
        total = viajes * (tarifa_maxima * 0.80)
    return total

def main() -> None:
    '''
    Función principal, donde el usuario ingresa la cantidad de viajes realizados

    Pre:
        la función no recibe parámetros
    Post:
        la función no devuelve ningún valor
    '''
    
    while True:
        try:
            viajes = int(input("Cantidad de viajes realizados: "))

            if viajes > 1:
                total = calcular_gastos(viajes)
                print(f"El total gastado en {viajes} viajes es de ${total} :)")
            else:
                print(f"ERROR. Intenta con una cantidad de viajes positiva.")
        except ValueError:
            print("ERROR. Intenta ingresando un número entero.")
    return None

main()