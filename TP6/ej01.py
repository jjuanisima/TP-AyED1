'''
Escribir un programa que lea un archivo de texto conteniendo un conjunto de ape
llidos y nombres en formato "Apellido, Nombre" y guarde en el archivo 
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cade
na "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los 
terminados en "EZ". Descartar el resto. Ejemplo:
 Arslanian, Gustavo–> ARMENIA.TXT
 Rossini, Giuseppe–> ITALIA.TXT
 Pérez, Juan
 Smith, John–> ESPAÑA.TXT–> descartar
 El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor.
'''


def registrar_apellidos() -> None:
    '''
    Registra los apellidos del archivo 'nombres.txt' en archivos separados de acuerdo a su origen

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    try:
        with open(r'TP6\armenia.txt', 'w', encoding='utf-8') as armenia, \
        open(r'TP6\españa.txt', 'w', encoding='utf-8') as espana, \
        open(r'TP6\italia.txt', 'w', encoding='utf-8') as italia:

            with open(r'TP6\nombres.txt', 'r', encoding='utf-8') as nombres:
                for linea in nombres:
                    linea = linea.strip()
                    apellido, nombre = linea.split(', ')

                    if apellido[-3:] == 'ian':
                        armenia.write(linea + '\n')
                    elif apellido[-2:] == 'ez':
                        espana.write(linea + '\n')
                    elif apellido[-3:] == 'ini':
                        italia.write(linea + '\n')
    except FileNotFoundError:
        print("No se encontró el archivo :(")

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    registrar_apellidos()

main()