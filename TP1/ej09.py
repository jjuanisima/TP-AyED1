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


import random as rn

def contar_naranjas(cant_naranjas):
    cajones = 0
    naranjas_jugo = 0
    peso_total = 0

    for i in range(cant_naranjas):
        peso_naranja = rn.randint(150, 350)

        if peso_naranja >= 200 and peso_naranja <= 300:
            peso_total += peso_naranja
            if peso_total >= 500000:
                cajones += 1
                peso_total = 0
        else:
            naranjas_jugo += 1  

    sobrantes = peso_total // 100
    return cajones, naranjas_jugo, sobrantes

def calcular_camiones(cajones):
    capacidad_camion = 500
    camiones = cajones // capacidad_camion
    if cajones % capacidad_camion != 0:
        camiones += 1
    return camiones

def main() -> None:
    try:
        cant_naranjas = int(input("Cantidad de naranjas cosechadas: "))

        cajones, naranjas_jugo, sobrantes = contar_naranjas(cant_naranjas)
        camiones = calcular_camiones(cajones)
        print(f"Cajones llenos: {cajones}")
        print(f"Naranjas para jugo: {naranjas_jugo}")
        print(f"Naranjas sobrantes: {sobrantes}")
        print(f"Camiones necesarios: {camiones}")
    except ValueError:
        print("ERROR. Revisa que la cantidad de naranjas sea un número entero.")
    return None

main()