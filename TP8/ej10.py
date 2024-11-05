'''
Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario 
y una lista de claves. La función debe eliminar del diccionario todas las claves 
contenidas en la lista, devolviendo el diccionario modificado y un número entero 
que represente la cantidad de claves eliminadas. Desarrollar también un programa 
para verificar su comportamiento.
'''


def eliminarclaves(diccionario: dict, claves: list) -> tuple:
    '''
    Elimina las claves del diccionario que también están en la lista de claves

    Pre:
        diccionario (dict): el diccionario del que se van a eliminar las claves
        claves (list): la lista de claves que se desean eliminar del diccionario
    Post:
        una tupla con el diccionario modificado y un entero que representa la cantidad de claves eliminadas
    '''

    claves_eliminadas = 0
    for clave in claves:
        if clave in diccionario:
            diccionario.pop(clave)
            claves_eliminadas += 1
    return diccionario, claves_eliminadas

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa

    Esta función no recibe parámetros y no devuelve ningún valor
    '''

    diccionario = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"}
    claves = [1, 3, 5, 7, 9]
    diccionario_final, cant_claves = eliminarclaves(diccionario, claves)

    print(f"Diccionario final: {diccionario_final}")
    print(f"Cantidad de claves eliminadas: {cant_claves}")

main()