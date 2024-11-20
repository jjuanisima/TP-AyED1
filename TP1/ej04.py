'''
Un comercio de electrodomésticos necesita para su línea de cajas un programa que 
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan 
dos números enteros, correspondientes al total de la compra y al dinero recibido. 
Informar cuántos billetes de cada denominación deben ser entregados como vuelto, 
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes 
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el 
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta 
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se 
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 
billete de $200, 1 billete de $100 y 3 billetes de $10.
'''


def calcular_cambio(vuelto: int) -> list:
    '''
    Calcula cuánto cambio se tiene que devolver, considerando los billetes existentes

    Pre:
        vuelto (int): el vuelto a calcular en billetes
    Post:
        devuelve una lista de tuplas (cantidad, billete) para el vuelto
    '''

    billetes = (5000, 1000, 500, 200, 100, 50, 10)

    billetes_vuelto = []
    for billete in billetes:
        cantidad = vuelto // billete
        if cantidad > 0:
            billetes_vuelto.append((cantidad, billete))
        vuelto %= billete
    
    return billetes_vuelto

if __name__ == "__main__":
    try:
        total_compra = int(input("Total de la compra: "))
        dinero_recibido = int(input("Dinero recibido: "))

        if dinero_recibido < total_compra:
            print("ERROR. El dinero recibido es insuficiente :|")
        else:
            vuelto = dinero_recibido - total_compra
            if vuelto == 0:
                print("No hay cambio que devolver :)")
            elif vuelto % 10 != 0:
                print("No es posible dar el cambio exacto con los billetes disponibles :(")
            else:
                print(f"\nEl cambio total es de ${vuelto}:")
                resultado = calcular_cambio(vuelto)
                for cant, billete in resultado:
                    print(f"{cant} billete(s) de ${billete}")
    except ValueError:
        print("ERROR. Revisa que los valores de compra y dinero recibido sean números enteros :|")