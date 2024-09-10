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


def calcular_cambio(total_compra: int, dinero_recibido: int) -> str:
    '''
    Calcula cuánto cambio se tiene que devolver, considerando los billetes existentes

    Pre:
        total_compra (int): el monto total de la compra
        dinero_recibido (int): el dinero recibido (puede ser mayor al monto de la compra)
    Post:
        str: cantidad de billetes de vuelto
    '''

    billetes = (5000, 1000, 500, 200, 100, 50, 10)
    
    if total_compra > dinero_recibido:
        return f"ERROR. El dinero recibido es insuficiente."

    vuelto = dinero_recibido - total_compra
    billetes_vuelto = []

    for i in range(len(billetes)):
        cant_billetes = vuelto // billetes[i]
        billetes_vuelto.append(cant_billetes)
        vuelto -= cant_billetes * billetes[i]

    if vuelto > 0:
        return f"ERROR. No se puede dar el cambio restante con los billetes disponibles :("

    for i in range(len(billetes)):
        if billetes_vuelto[i] > 0:
            print(f"{billetes_vuelto[i]} billete(s) de ${billetes[i]}")

def main() -> None:
    '''
    Función principal, donde el usuario ingresa el total de la compra y el dinero recibido

    Pre:
        la función no recibe parámetros
    Post:
        la función no devuelve ningún valor
    '''

    try:
        total_compra = int(input("Total de la compra: "))
        dinero_recibido = int(input("Dinero recibido: "))
        print(calcular_cambio(total_compra, dinero_recibido))
    except ValueError:
        print("ERROR. Revisa que los valores de compra y dinero recibido sean números enteros.")
    return None

main()