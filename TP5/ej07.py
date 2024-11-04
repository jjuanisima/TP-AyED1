'''
Escribir un programa que juegue con el usuario a adivinar un número. El programa 
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para 
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el nú
mero que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga 
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar 
el número. Si el usuario introduce algo que no sea un número se mostrará un 
mensaje en pantalla y se lo contará como un intento más.
'''


from typing import Tuple
from random import randint

def buscar_numero(num: int, numero_a_adivinar: int, intentos: int) -> Tuple [str, int]:
    '''
    Compara el número a adivinar con el ingresado por el usuario, y retorna el mensaje correspondiente y la cantidad de intentos

    Pre:
        num (int): el número ingresado por el usuario
        numero_a_adivinar (int): el número random a adivinar
        intentos (int): los intentos que lleva el usuario intentando adivinar el número 
    Post:
        una tupla con el mensaje para el usuario y el contador de los intentos
    '''

    if num < numero_a_adivinar:
        intentos += 1
        return "Una pista, el número a encontrar es más grande :)", intentos
    elif num > numero_a_adivinar:
        intentos += 1
        return "Una pista, el número a encontrar es más chiquito :)", intentos
    else:
        intentos += 1
        return "¡Adivinaste el número! :)", intentos

def main() -> None:
    '''
    Función principal, donde el usuario intenta adivinar el número generado por el programa

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    intentos = 0
    numero_a_adivinar = randint(1, 500)

    while True:
        try:
            num = int(input("Ingrese un número: "))
            mensaje, intentos = buscar_numero(num, numero_a_adivinar, intentos)
            print(mensaje)

            if num == numero_a_adivinar:
                print(f"Intentos: {intentos}")
                break
        except ValueError:
            intentos += 1
            print("ERROR. Revisa de ingresar un número :|")

main()