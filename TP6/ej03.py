'''
Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los 
próximos Juegos Panamericanos. Para eso encargó la realización de un programa 
que incluya las siguientes funciones:
 GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas 
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una 
línea distinta. Ejemplo:
 <Deporte 1>
 <altura del atleta 1>
 <altura del atleta 2>
 < . . . >
 <Deporte 2>
 <altura del atleta 1>
 <altura del atleta 2>
 < . . . >
 GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atle
tas, leyendo los datos del archivo generado en el paso anterior. La disciplina y el 
promedio deben grabarse en líneas diferentes. Ejemplo:
 <Deporte 1>
 <Promedio de alturas deporte 1>
 <Deporte 2>
 <Promedio de alturas deporte 2>
 < . . . >
  MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas 
superan la estatura promedio general. Obtener los datos del segundo archivo.
'''


def grabarrangoalturas() -> None:
    '''
    Se ingresan deportes y alturas y se guarda la información en un archivo llamado 'alturas.txt'

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    with open('TP6/alturas.txt', 'w', encoding='utf-8') as alturas:
        while True:
            deporte = input("Ingrese el deporte ('S' para salir): ").strip()
            if deporte.upper() == 'S':
                print(f"Registro finalizado :)")
                break
            alturas.write(deporte.capitalize() + '\n')

            while True:
                altura = input("Ingrese la altura ('S' para salir): ").strip()
                if altura.upper() == 'S':
                    print(f"Registro de {deporte} finalizado :)")
                    break
                alturas.write(altura + '\n')
            alturas.write('\n')

def grabarpromedio() -> None:
    '''
    Lee alturas del archivo 'alturas.txt' y calcula promedios, guardándolos en otro archivo llamado 'promedios.txt'

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    with open('TP6/alturas.txt', 'r', encoding='utf-8') as alturas, open('TP6/promedios.txt', 'w', encoding='utf-8') as promedios:
        registro_alturas = []
        for linea in alturas:
          linea = linea.strip()
          
          try:
              altura = float(linea)
              registro_alturas.append(altura)
          except ValueError:
              if registro_alturas:
                  promedio = sum(registro_alturas) / len(registro_alturas)
                  promedios.write(f"{promedio}")
                  registro_alturas = []
              promedios.write(linea + '\n')
              
def mostrarmasaltos() -> None:
    '''
    Muestra los deportes cuyos atletas superan la altura promedio

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    with open('TP6/promedios.txt', 'r', encoding='utf-8') as promedios:
        registro_promedios = []
        deportes = []

        for linea in promedios:
            linea = linea.strip()

            try:
                promedio = float(linea)
                registro_promedios.append(promedio)
            except ValueError:
                if linea:
                    deportes.append(linea)

        if registro_promedios:
          max_promedio = sum(registro_promedios) / len(registro_promedios)
          print(f"\nPromedio general: {max_promedio:.2f}")
          print("Deportes cuyos atletas superan la altura promedio:")

          for i in range(len(registro_promedios)):
              if registro_promedios[i] > max_promedio:
                  print(deportes[i])
        else:
            print("No se encontraron promedios válidos en el archivo :(")

if __name__ == "__main__":
    grabarrangoalturas()
    grabarpromedio()
    mostrarmasaltos()