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
        devuelve el total gastado en viajes
    '''
    tarifa_maxima = 650.0

    if viajes > 40:
        return viajes * (tarifa_maxima * 0.60)
    elif viajes >= 31 and viajes <= 40:
        return viajes * (tarifa_maxima * 0.70)
    elif viajes >= 21 and viajes <= 30:
        return viajes * (tarifa_maxima * 0.80)
    else:
        return viajes * tarifa_maxima

def main() -> None:
    '''
    Función principal que maneja el flujo del programa
    No recibe parámetros ni devuelve ningún valor
    '''
    try:
        viajes = int(input("Cantidad de viajes realizados: "))
    except ValueError:
        print("ERROR. Intenta ingresando un número entero.")

    if viajes < 1:
        print("ERROR. Ingresa una cantidad válida de viajes :|")
    else:
        total = calcular_gastos(viajes)
        print(f"El total gastado en {viajes} viajes es de ${total} :)")
        
if __name__ == "__main__":
    main()