'''
Se solicita crear un programa para leer direcciones de correo electrónico y verificar 
si representan una dirección válida. Por ejemplo 
usuario@dominio.com.ar. Para que 
una dirección sea considerada válida el nombre de usuario debe poseer solamente 
caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe 
tener al menos un carácter y tiene que finalizar con .com o .com.ar.  
Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mos
trar un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente, 
recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas.
'''


import re

def validar_correo(correo: str) -> bool:
    '''
    Verifica si la dirección de correo electrónico es válida según el patrón especificado

    Pre:
        correo (str): el correo electrónico a validad
    Post:
        true: el correo es válido
        false: el correo es inválido
    '''

    patron = "^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|com.ar)$"
    return re.match(patron, correo)
    
def main() -> None:
    '''
    Función principal, donde el usuario ingresa el correo electrónico a validar
    '''
    
    dominios = []
    while True:
        correo = input("Correo electrónico: ")

        if correo == "":
            break

        if validar_correo(correo):
            usuario, dominio = correo.split('@')
            if dominio not in dominios:
                dominios.append(dominio)
            print(f"{correo} es válido :)")
        else:
            print("ERROR. Correo inválido :(")

    if dominios:
        print("\nDominios únicos:")
        for dominio in sorted(dominios):
            print(dominio)
    else:
        print("No hay dominios válidos.")

main()