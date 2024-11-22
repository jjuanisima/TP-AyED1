'''
Se dispone de tres formatos diferentes de archivos de texto en los que se almace
nan datos de empleados, detallados más abajo. Desarrollar un programa para cada 
uno de los formatos suministrados, que permitan leer cada uno de los archivos y 
grabar los datos obtenidos en otro archivo de texto con formato CSV.
'''


import csv

def leer_archivo1() -> None:
    '''
    Lee el archivo 'empleados1.txt' y guarda los datos en un nuevo archivo 'empleados1.1.csv'

    Esta función no recibe parámetros ni devuelve ningún valor
    '''
    
    with open('TP6\empleados1.txt', 'r', encoding='utf-8') as archivo1:
        lineas = archivo1.readlines()

    nombres = []
    for linea in lineas:
        linea = linea.rstrip()

        nombre = []
        nombre.append(linea[:17].strip())
        nombre.append(linea[17:26].strip())
        nombre.append(linea[26:].strip())

        nombres.append(nombre)

    with open('TP6\empleados1.1.csv', 'w', newline='', encoding='utf-8') as archivo1csv:
        writer = csv.writer(archivo1csv)
        writer.writerow(["Nombre", "Legajo", "Dirección"])
        writer.writerows(nombres)

if __name__ == "__main__":
    leer_archivo1()