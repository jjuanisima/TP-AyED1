'''
Resolver el siguiente problema utilizando funciones:
    Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso 
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y 
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón 
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso 
de alguna naranja se encuentra fuera del rango indicado se la clasifica para 
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas 
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para 
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente 
reparto. Simular el peso de cada unidad generando un número entero al azar entre 
150 y 350.
    Además, se desea saber cuántos camiones se necesitan para transportar la cose
cha, considerando que la ocupación del camión no debe ser inferior al 80%; en 
caso contrario el camión no serán despachado por su alto costo. 
'''


import math
import random as rn

def contar_naranjas(cant_naranjas: int) -> tuple:
    '''
    Cuenta las naranjas según el peso. Si pesan entre 200 y 300 gramos van al cajón, si su peso está fuera de ese rango se clasifican para jugo, y se consideran las naranjas sobrantes

    Pre:
        cant_naranjas (int): cantidad de naranjas cosechadas
    Post:
        devuelve una tupla con la cant. de cajones llenos, la cant. de naranjas para jugo, la cant. de naranjas sobrantes y el peso total
    '''
    
    cajones = 0
    naranjas_jugo = 0
    naranjas_cajon = 0
    peso_total = 0

    for _ in range(cant_naranjas):
        peso_naranja = rn.randint(150, 350)

        if peso_naranja >= 200 and peso_naranja <= 300:
            naranjas_cajon += 1
            peso_total += peso_naranja

            if naranjas_cajon == 100:
                cajones += 1
                naranjas_cajon = 0
        else:
            naranjas_jugo += 1

    sobrantes = naranjas_cajon
    return cajones, naranjas_jugo, sobrantes, peso_total

def calcular_camiones(peso_total: int) -> int:
    '''
    Calcula la cantidad de camiones necesarios

    Pre:
        cajones (int): cantidad de cajones que hay que guardar en los camiones
    Post:
        devuelve la cantidad de camiones necesarios para transportar la cosecha
    '''

    capacidad_camion = 500000
    ocupacion_minima = 0.8 * capacidad_camion

    if peso_total < ocupacion_minima:
        return 0
    
    camiones = math.ceil(peso_total / capacidad_camion)
    return camiones

if __name__ == "__main__":
    try:
        cant_naranjas = int(input("Cantidad de naranjas cosechadas: "))
        if cant_naranjas <= 0:
            print("Revisa que la cantidad de naranjas sea mayor que cero :|")
        else:
            cajones, naranjas_jugo, sobrantes, peso_total = contar_naranjas(cant_naranjas)
            camiones = calcular_camiones(peso_total)

            print(f"\nCajones llenos: {cajones}")
            print(f"Naranjas para jugo: {naranjas_jugo}")
            print(f"Naranjas sobrantes: {sobrantes}")
            print(f"Camiones necesarios (80% ocupación mínima): {camiones}")
    except ValueError:
        print("ERROR. Revisa que la cantidad de naranjas sea un número entero.")