'''
Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al 
usuario y eliminarlos del conjunto mediante el método remove, mostrando el con
tenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1. 
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos 
inexistentes.
'''


def eliminar_numero(conjunto: set, num_a_eliminar: int):
    '''
    Elimina un número del conjunto dado

    Pre:
        conjunto (set): el conjunto del que se quiere eliminar el número
        num_a_eliminar (int): el número que se quiere eliminar
    Post:
        el conjunto actualizado después de eliminar el número. En caso de que el número no exista, se levanta un KeyError
    '''
    
    try:
        conjunto.remove(num_a_eliminar)
        return conjunto
    except KeyError:
        print(f"ERROR. El número {num_a_eliminar} no existe en el conjunto :|")
        return conjunto

if __name__ == "__main__":
    conjunto = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    print(conjunto)
    while True:
        try:
            num_a_eliminar = int(input("Número a eliminar (-1 para salir): "))
        except ValueError:
            print("ERROR. Revisa de ingresar un número válido :|")
        else:
            if num_a_eliminar == -1:
                print("Saliendo...")
                break

            print(f"\nConjunto actualizado: {eliminar_numero(conjunto, num_a_eliminar)}") if len(conjunto) > 0 else print("El conjunto está vacío :|")