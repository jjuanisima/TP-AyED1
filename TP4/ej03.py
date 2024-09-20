'''
Los números de claves de dos cajas fuertes están intercalados dentro de un número 
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa 
para obtener ambas claves, donde la primera se construye con los dígitos ubicados 
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en 
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave 
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.
'''


def desglosar_clave(clave_maestra) -> tuple:
    '''
    Desglosa la clave maestra en dígitos en posiciones impares y pares
    Pre:
        clave_maestra (str): la clave ingresada por el usuario
    Post:
        impares, pares (tuple): una tupla con los valores pares (impares) e impares (pares)
    '''

    impares = ""
    pares = ""
    
    for i in range(len(clave_maestra)):
        if i % 2 == 0:
            impares += clave_maestra[i]
        else:
            pares += clave_maestra[i]
    return impares, pares

def main() -> None:
    '''
    Función principal, donde el usuario ingresa una cadena y se ejecuta el programa
    '''
    
    clave_maestra = input("Clave maestra: ")
    impares, pares = desglosar_clave(clave_maestra)
    print(f"Clave 1: {impares}")
    print(f"Clave 2: {pares}")
    return None

main()