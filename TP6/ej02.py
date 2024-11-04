'''
Escribir un programa que permita dividir un archivo de texto cualquiera en partes 
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se 
ingresa por teclado. Los nombres de los archivos generados deben respetar el 
nombre original con el agregado de un sufijo que indique de qué parte se trata. 
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuar
se después del delimitador del mismo. Mostrar un mensaje de error si el proceso no 
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en 
memoria.
'''


from math import ceil

def dividir_archivo(partes) -> None:
    '''
    Divide el contenido del archivo 'archivocorreo.txt' en una n cantidad de fragmentos

    Pre:
        partes (int): tamaño máximo de caracteres de cada fragmento
    Post:
        no devuelve ningún valor
    '''

    try:
        with open(r'TP6\archivocorreo.txt', 'r', encoding='utf-8') as correo:
            contenido = correo.read()
            longitud = len(contenido)
            sufijo = 0
            
            try:
                if partes > longitud:
                    raise ValueError("ERROR. La cantidad de caracteres es mayor que la longitud del texto :|")
                
                cant_fragmentos = ceil(longitud / partes)
                
                for i in range(cant_fragmentos):
                    fragmento = contenido[:partes]
                    contenido = contenido[partes:]
                    sufijo += 1
                    
                    archivo = f'TP6\\archivocorreo{sufijo}.txt'
                    with open(archivo, 'w', encoding='utf-8') as partes_correo:
                        partes_correo.write(fragmento)

            except ValueError as m:
                print(m)

    except FileNotFoundError:
        print("No se encontró el archivo :(")

def main() -> None:
    '''
    Función principal, donde el usuario ingresa el tamaño de las partes en las que dividir el archivo

    Esta función no recibe parámetros y no devuelve ningún valor
    '''
    
    partes = int(input("Tamaño máximo de las partes a dividir el archivo: "))
    dividir_archivo(partes)

main()