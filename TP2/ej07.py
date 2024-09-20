'''
Intercalar los elementos de una lista entre los elementos de otra. La intercalación 
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará 
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] 
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden 
tener distintas longitudes.
'''


def intercalar_listas(lista1, lista2) -> list:
    '''
    Agrega a la lista1 los elementos de la lista2 de manera intercalada

    Pre:
        lista1 (list): la lista1
        lista2 (list): la lista2
    Post:
        lista1 (list): la lista1 con los elementos intercalados de la lista2
    '''

    for i in range(len(lista2)):
        lista1.insert(2 * i + 1, lista2[i])
    return lista1

def main() -> None:
    '''
    Función principal, donde se ejecuta el programa
    '''
    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7]
    print(intercalar_listas(lista1, lista2))

main()