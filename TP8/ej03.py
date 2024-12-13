'''
Desarrollar un programa que utilice una función que reciba como parámetro una 
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva 
una tupla con las distintas partes que componen dicha dirección. Ejemplo: 
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar 
formatos de fecha inválidos y devolver una tupla vacía.
'''


import re

def partes_correo(correo: str) -> tuple:
    '''
    Descompone una dirección de correo electrónico en sus partes

    Pre:
        correo (str): la dirección de correo a descomponer
    Post:
        devuelve una tupla con el usuario y las partes del dominio, en caso contrario una tupla vacía
    '''

    if not re.match('^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$', correo):
        return ()
    
    usuario, dominio = correo.split('@')
    partes_dominio = dominio.split('.')

    return usuario, *partes_dominio

if __name__ == "__main__":
    correo = input("Correo electrónico: ")

    print(f"{correo} -> {partes_correo(correo)}") if partes_correo(correo) else print("Correo inválido :|")